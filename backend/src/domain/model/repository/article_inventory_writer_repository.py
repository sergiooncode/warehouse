from abc import ABC
from abc import abstractmethod


class ArticleInventoryWriterRepository(ABC):
    @abstractmethod
    def remove_inventory_by_id_and_amount(self, article_id: str) -> None:
        pass
