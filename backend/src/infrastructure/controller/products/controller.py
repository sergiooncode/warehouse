from http import HTTPStatus

from flask import current_app
from flask import request
from flask_restx import Resource
from src.infrastructure.controller.base import api

from src.infrastructure.persistence.inmemory.repository.inmemory_article_inventory_reader_repository import (
    InmemoryArticleInventoryReaderRepository,
)
from src.infrastructure.persistence.inmemory.repository.inmemory_canonical_product_reader_repository import (
    InmemoryCanonicalProductReaderRepository,
)
from src.application.use_case.calculate_products_availability_service import (
    CalculateProductAvailabilityService,
)
from src.application.use_case.update_inventory_service import UpdateInventoryService
from src.infrastructure.persistence.inmemory.repository.inventory_article_inventory_writer_repository import (
    InmemoryArticleInventoryWriterRepository,
)

products_ns = api.namespace("products", description="Products")


@products_ns.route("", endpoint="products")
class ProductsController(Resource):
    def __init__(self, *args, **kwargs):
        self.__session = current_app.config["WAREHOUSE_STORE"]
        self.__product_availability_service: CalculateProductAvailabilityService = CalculateProductAvailabilityService(
            canonical_product_reader_repository=InmemoryCanonicalProductReaderRepository(
                self.__session
            ),
            article_inventory_reader_repository=InmemoryArticleInventoryReaderRepository(
                self.__session
            ),
        )
        self.__inventory_update_service: UpdateInventoryService = UpdateInventoryService(
            canonical_product_reader_repository=InmemoryCanonicalProductReaderRepository(
                self.__session
            ),
            article_inventory_writer_repository=InmemoryArticleInventoryWriterRepository(
                self.__session
            ),
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

        if not self.__is_there_enough_product_availability_for(
            product_name, units_to_sell, product_availability
        ):
            return api.abort(HTTPStatus.UNPROCESSABLE_ENTITY, "Not enough product availability")
        self.__inventory_update_service.execute(
            product_name=product_name, product_units_to_sell=units_to_sell
        )
        return dict(
            message="Product ordered fulfilled"
        )

    def __is_there_enough_product_availability_for(
        self, product_name, units_to_sell, product_availability
    ):
        return units_to_sell <= product_availability[product_name].availability_in_units
