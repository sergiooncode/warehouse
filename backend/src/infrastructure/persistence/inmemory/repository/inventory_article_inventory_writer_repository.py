from typing import Dict

from src.domain.model.repository.article_inventory_writer_repository import (
    ArticleInventoryWriterRepository,
)


class InmemoryArticleInventoryWriterRepository(ArticleInventoryWriterRepository):
    def __init__(self, session: Dict):
        self.__session = session

    def remove_inventory_by_id_and_amount(self, article_id: str, amount: int) -> None:
        self.__session["inventory"][article_id].stock -= amount
