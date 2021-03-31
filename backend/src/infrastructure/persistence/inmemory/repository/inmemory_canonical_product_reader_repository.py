from typing import Dict
from typing import List

from src.domain.model.canonical_product import CanonicalProduct
from src.domain.model.repository.canonical_product_reader_repository import (
    CanonicalProductReaderRepository,
)


class InmemoryCanonicalProductReaderRepository(CanonicalProductReaderRepository):
    def __init__(self, session: Dict):
        self.__session = session

    def list_all_products(self) -> Dict[str, CanonicalProduct]:
        return self.__session["products"]

    def list_products_by_product_names(
        self, names: List[str]
    ) -> Dict[str, CanonicalProduct]:
        canonical_products = {}
        for name in names:
            if name in self.__session["products"]:
                canonical_products[name] = self.__session["products"][name]
        return canonical_products
