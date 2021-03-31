from unittest import TestCase

from src.app import app


class TestProductsController(TestCase):
    def setUp(self) -> None:
        self.app = app
        self.app_client = app.test_client()

    def test_list_products(self):
        response = self.app_client.get("/products")

        expected_json = {
            "Dining Chair": {"availability_in_units": 2, "price": 100},
            "Dinning Table": {"availability_in_units": 1, "price": 100},
        }

        self.assertEqual(expected_json, response.json)
