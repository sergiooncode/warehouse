from abc import ABC
from abc import abstractmethod
from typing import Dict
from typing import List

from src.domain.model.canonical_product import CanonicalProduct


class CanonicalProductReaderRepository(ABC):
    @abstractmethod
    def list_all_products(self) -> Dict[str, CanonicalProduct]:
        pass

    @abstractmethod
    def list_products_by_product_names(
        self, names: List[str]
    ) -> Dict[str, CanonicalProduct]:
        pass
