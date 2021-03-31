from typing import Dict
from typing import List

from src.domain.model.canonical_article import CanonicalArticle
from src.domain.model.canonical_product import CanonicalProduct
from src.domain.model.repository.canonical_product_reader_repository import (
    CanonicalProductReaderRepository,
)
from src.infrastructure.persistence.mongoengine.model.canonical_product import MongoCanonicalProduct


class MongoengineCanonicalProductReaderRepository(CanonicalProductReaderRepository):
    def list_all_products(self) -> Dict[str, CanonicalProduct]:
        canonical_product_objects = MongoCanonicalProduct.objects.all()
        return [
            CanonicalProduct(
                name=o.name,
                price=o.price,
                containing_articles=[
                    CanonicalArticle(
                        article_id=ca.article_id,
                        needed_amount=ca.needed_amount
                    )
                    for ca in o.containing_articles
                ]
            )
            for o in canonical_product_objects
        ]

    def list_products_by_product_names(
        self, names: List[str]
    ) -> Dict[str, CanonicalProduct]:
        canonical_product_objects = MongoCanonicalProduct.objects(name__in=names).all()
        return [
            CanonicalProduct(
                name=o.name,
                price=o.price,
                containing_articles=[
                    CanonicalArticle(
                        article_id=ca.article_id,
                        needed_amount=ca.needed_amount
                    )
                    for ca in o.containing_articles
                ]
            )
            for o in canonical_product_objects
        ]
