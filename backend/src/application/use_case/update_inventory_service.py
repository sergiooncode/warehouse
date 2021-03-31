from src.domain.model.repository.article_inventory_writer_repository import (
    ArticleInventoryWriterRepository,
)
from src.domain.model.repository.canonical_product_reader_repository import (
    CanonicalProductReaderRepository,
)


class UpdateInventoryService:
    def __init__(
        self,
        canonical_product_reader_repository: CanonicalProductReaderRepository,
        article_inventory_writer_repository: ArticleInventoryWriterRepository,
    ):
        self.__canonical_product_reader_repository = canonical_product_reader_repository
        self.__article_inventory_reader_repository = article_inventory_writer_repository

    def execute(self, product_name: str, product_units_to_sell: int) -> None:
        canonical_products = (
            self.__canonical_product_reader_repository.list_products_by_product_names(
                [product_name]
            )
        )

        for containing_article in canonical_products[product_name].containing_articles:
            self.__article_inventory_reader_repository.remove_inventory_by_id_and_amount(
                containing_article.article_id,
                product_units_to_sell * containing_article.needed_amount,
            )
