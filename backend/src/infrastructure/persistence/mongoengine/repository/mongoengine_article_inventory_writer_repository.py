from src.domain.model.repository.article_inventory_writer_repository import (
    ArticleInventoryWriterRepository,
)

from src.infrastructure.persistence.mongoengine.model.article_inventory import (
    MongoArticleInventory,
)


class MongoengineArticleInventoryWriterRepository(ArticleInventoryWriterRepository):
    def remove_inventory_by_id_and_amount(self, article_id: str, amount: int) -> None:
        current_stock = (
            MongoArticleInventory.objects(article_id=article_id).all()[0].stock
        )
        MongoArticleInventory.objects(article_id=article_id).update(
            set__stock=current_stock - amount
        )
