from unittest import TestCase
from unittest.mock import Mock

from src.application.use_case.calculate_products_availability_service import (
    CalculateProductAvailabilityService,
)
from src.domain.model.article_inventory import ArticleInventory
from src.domain.model.canonical_article import CanonicalArticle
from src.domain.model.canonical_product import CanonicalProduct
from src.infrastructure.persistence.inmemory.repository.inmemory_article_inventory_reader_repository import (
    InmemoryArticleInventoryReaderRepository,
)
from src.infrastructure.persistence.inmemory.repository.inmemory_canonical_product_reader_repository import (
    InmemoryCanonicalProductReaderRepository,
)


class TestCalculateProductAvailabilityUseCase(TestCase):
    def setUp(self) -> None:
        self.canonical_product_reader_repository = Mock(
            spec=InmemoryCanonicalProductReaderRepository
        )
        self.canonical_product_reader_repository.list_all_products.return_value = {
            "2 x Glass Box": CanonicalProduct(
                name="2 x Glass Box",
                price=6,
                containing_articles=[
                    CanonicalArticle(article_id="11", needed_amount=2)
                ],
            )
        }
        self.canonical_product_reader_repository.list_products_by_product_names.return_value = {
            "2 x Glass Box": CanonicalProduct(
                name="2 x Glass Box",
                price=6,
                containing_articles=[
                    CanonicalArticle(article_id="11", needed_amount=2)
                ],
            )
        }
        self.article_inventory_reader_repository = Mock(
            spec=InmemoryArticleInventoryReaderRepository
        )
        self.article_inventory_reader_repository.detail_inventory_by_id.return_value = (
            ArticleInventory(article_id="11", name="glass", stock=3)
        )
        self.service = CalculateProductAvailabilityService(
            canonical_product_reader_repository=self.canonical_product_reader_repository,
            article_inventory_reader_repository=self.article_inventory_reader_repository,
        )

    def test_calculate(self):
        product_availability = self.service.execute()
        self.assertEqual("2 x Glass Box", product_availability["2 x Glass Box"].name)
        self.assertEqual(1, product_availability["2 x Glass Box"].availability_in_units)
