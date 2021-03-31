from typing import Dict

from src.domain.model.product import Product
from src.domain.model.repository.canonical_product_reader_repository import (
    CanonicalProductReaderRepository,
)
from src.domain.model.repository.article_inventory_reader_repository import (
    ArticleInventoryReaderRepository,
)


class CalculateProductAvailabilityService:
    def __init__(
        self,
        canonical_product_reader_repository: CanonicalProductReaderRepository,
        article_inventory_reader_repository: ArticleInventoryReaderRepository,
    ):
        self.__canonical_product_reader_repository: CanonicalProductReaderRepository = (
            canonical_product_reader_repository
        )
        self.__article_inventory_reader_repository: ArticleInventoryReaderRepository = (
            article_inventory_reader_repository
        )

    def execute(self) -> Dict[str, Product]:
        product_availability = {}

        all_canonical_products = (
            self.__canonical_product_reader_repository.list_all_products()
        )

        for product_name in all_canonical_products:
            intermediate_availability = self.__calculate_whole_containing_articles(
                all_canonical_products, product_name
            )
            availability_in_units = min(intermediate_availability)
            product_availability[product_name] = Product(
                name=product_name,
                price=all_canonical_products[product_name].price,
                availability_in_units=availability_in_units,
            )

        return product_availability

    def __calculate_whole_containing_articles(
        self, all_canonical_products, product_name
    ):
        """
        Calculate whole division between stock of inventory for an article and
        the needed amount of that articles in a canonical product
        :param all_canonical_products:
        :param product_name:
        :return: list of amounts for each containing article in a canonical product
        """
        intermediate_availability = [
            self.__article_inventory_reader_repository.detail_inventory_by_id(
                canonical_article.article_id
            ).stock
            // canonical_article.needed_amount
            for canonical_article in all_canonical_products[
                product_name
            ].containing_articles
        ]
        return intermediate_availability
