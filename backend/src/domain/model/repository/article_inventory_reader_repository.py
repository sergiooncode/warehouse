from abc import ABC
from abc import abstractmethod

from src.domain.model.article_inventory import ArticleInventory


class ArticleInventoryReaderRepository(ABC):
    @abstractmethod
    def detail_inventory_by_id(self, article_id: str) -> ArticleInventory:
        pass
