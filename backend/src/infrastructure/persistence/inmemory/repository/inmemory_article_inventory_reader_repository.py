from typing import Dict

from src.domain.model.article_inventory import ArticleInventory
from src.domain.model.repository.article_inventory_reader_repository import (
    ArticleInventoryReaderRepository,
)


class InmemoryArticleInventoryReaderRepository(ArticleInventoryReaderRepository):
    def __init__(self, session: Dict):
        self.__session = session

    def detail_inventory_by_id(self, article_id: str) -> ArticleInventory:
        return self.__session["inventory"][article_id]
