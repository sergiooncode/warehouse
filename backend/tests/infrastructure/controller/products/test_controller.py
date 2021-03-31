import json
from unittest import TestCase

from src.app import app
from src.infrastructure.persistence.mongoengine.model.article_inventory import (
    MongoArticleInventory,
)

from bin.cli.seed_data import load_mongo_seed_data


class TestProductsController(TestCase):
    def setUp(self) -> None:
        self.app = app
        self.app_client = app.test_client()
        load_mongo_seed_data(loading_message=False)

    def test_list_products(self):
        response = self.app_client.get("/products")

        expected_json = {
            "Dining Chair": {"availability_in_units": 2, "price": 100},
            "Dinning Table": {"availability_in_units": 1, "price": 100},
        }

        self.assertEqual(expected_json, response.json)

    def test_sell_products_no_availability(self):
        response = self.app_client.post(
            "/products",
            data=json.dumps({"product_name": "Dining Chair", "units_to_sell": 10}),
            content_type="application/json",
        )

        self.assertEqual("Not enough product availability", response.json["message"])
        self.assertEqual(422, response.status_code)

    def test_sell_products_enough_availability(self):
        response = self.app_client.post(
            "/products",
            data=json.dumps({"product_name": "Dining Chair", "units_to_sell": 1}),
            content_type="application/json",
        )

        self.assertEqual("Product ordered fulfilled", response.json["message"])
        self.assertEqual(200, response.status_code)
        self.assertEqual(
            8, MongoArticleInventory.objects(article_id="1").all()[0].stock
        )
        self.assertEqual(
            9, MongoArticleInventory.objects(article_id="2").all()[0].stock
        )
        self.assertEqual(
            1, MongoArticleInventory.objects(article_id="3").all()[0].stock
        )

    def test_sell_products_non_existant_product_name(self):
        response = self.app_client.post(
            "/products",
            data=json.dumps({"product_name": "Futon", "units_to_sell": 1}),
            content_type="application/json",
        )

        self.assertEqual("Product by that name doesnt exist", response.json["message"])
        self.assertEqual(400, response.status_code)

    def test_sell_products_units_to_sell_not_allowed(self):
        response = self.app_client.post(
            "/products",
            data=json.dumps({"product_name": "Dining Chair", "units_to_sell": 0}),
            content_type="application/json",
        )

        self.assertEqual("Number of units to sell not allowed", response.json["message"])
        self.assertEqual(400, response.status_code)
