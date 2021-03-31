from flask import current_app
from flask_restx import Resource
from src.infrastructure.controller.base import api

from src.infrastructure.persistence.inmemory.repository.inmemory_article_inventory_reader_repository import \
    InmemoryArticleInventoryReaderRepository
from src.infrastructure.persistence.inmemory.repository.inmemory_canonical_product_reader_repository import \
    InmemoryCanonicalProductReaderRepository

from src.application.use_case.calculate_products_availability_service import CalculateProductAvailabilityService

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
