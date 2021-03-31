from src.domain.model.article_inventory import ArticleInventory
from src.domain.model.repository.article_inventory_reader_repository import (
    ArticleInventoryReaderRepository,
)
from src.infrastructure.persistence.mongoengine.model.article_inventory import (
    MongoArticleInventory,
)


class MongoengineArticleInventoryReaderRepository(ArticleInventoryReaderRepository):
    def detail_inventory_by_id(self, article_id: str) -> ArticleInventory:
        article_inventory_object = MongoArticleInventory.objects(
            article_id=article_id
        ).all()[0]
        return ArticleInventory(
            article_id=article_inventory_object.article_id,
            name=article_inventory_object.name,
            stock=article_inventory_object.stock,
        )
