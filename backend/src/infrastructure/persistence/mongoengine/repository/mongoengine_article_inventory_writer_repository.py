from src.domain.model.repository.article_inventory_writer_repository import ArticleInventoryWriterRepository


class MongoengineArticleInventoryWriterRepository(ArticleInventoryWriterRepository):
    def remove_inventory_by_id_and_amount(self, article_id: str, amount: int) -> None:
        pass
