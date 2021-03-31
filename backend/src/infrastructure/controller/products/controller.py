from http import HTTPStatus

from flask import request
from flask_restx import Resource
from src.application.use_case.calculate_products_availability_service import (
    CalculateProductAvailabilityService,
)
from src.application.use_case.update_inventory_service import UpdateInventoryService
from src.infrastructure.controller.base import api
from src.infrastructure.persistence.mongoengine.repository.mongoengine_article_inventory_reader_repository import (
    MongoengineArticleInventoryReaderRepository,
)
from src.infrastructure.persistence.mongoengine.repository.mongoengine_article_inventory_writer_repository import (
    MongoengineArticleInventoryWriterRepository,
)
from src.infrastructure.persistence.mongoengine.repository.mongoengine_canonical_product_reader_repository import (
    MongoengineCanonicalProductReaderRepository,
)

products_ns = api.namespace("products", description="Products")


@products_ns.route("", endpoint="products")
class ProductsController(Resource):
    def __init__(self, *args, **kwargs):
        self.__product_availability_service: CalculateProductAvailabilityService = CalculateProductAvailabilityService(
            canonical_product_reader_repository=MongoengineCanonicalProductReaderRepository(),
            article_inventory_reader_repository=MongoengineArticleInventoryReaderRepository(),
        )
        self.__inventory_update_service: UpdateInventoryService = UpdateInventoryService(
            canonical_product_reader_repository=MongoengineCanonicalProductReaderRepository(),
            article_inventory_writer_repository=MongoengineArticleInventoryWriterRepository(),
        )

    def get(self):
        product_data = self.__product_availability_service.execute()
        response_data = {
            product_name: {
                "availability_in_units": product_data[
                    product_name
                ].availability_in_units,
                "price": product_data[product_name].price,
            }
            for product_name in product_data
        }
        return response_data

    def post(self):
        product_name = request.json["product_name"]
        units_to_sell = request.json["units_to_sell"]
        product_availability = self.__product_availability_service.execute(
            [product_name]
        )
        if product_name not in product_availability:
            api.abort(HTTPStatus.BAD_REQUEST, "Product by that name doesnt exist")
        if units_to_sell <= 0:
            api.abort(HTTPStatus.BAD_REQUEST, "Number of units to sell not allowed")

        if not self.__is_there_enough_product_availability_for(
            product_name, units_to_sell, product_availability
        ):
            return api.abort(
                HTTPStatus.UNPROCESSABLE_ENTITY, "Not enough product availability"
            )
        self.__inventory_update_service.execute(
            product_name=product_name, product_units_to_sell=units_to_sell
        )
        return dict(message="Product ordered fulfilled")

    def __is_there_enough_product_availability_for(
        self, product_name, units_to_sell, product_availability
    ):
        return units_to_sell <= product_availability[product_name].availability_in_units
