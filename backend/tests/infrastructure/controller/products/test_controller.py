import json
from copy import deepcopy
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

    def test_sell_products_no_availability(self):
        response = self.app_client.post(
            "/products",
            data=json.dumps({"product_name": "Dining Chair", "units_to_sell": 10}),
            content_type="application/json",
        )

        self.assertEqual("Not enough product availability", response.json["message"])
        self.assertEqual(422, response.json["status_code"])

    def test_sell_products_enough_availability(self):
        initial_inventory = deepcopy(self.app.config["WAREHOUSE_STORE"]["inventory"])

        response = self.app_client.post(
            "/products",
            data=json.dumps({"product_name": "Dining Chair", "units_to_sell": 1}),
            content_type="application/json",
        )

        self.assertEqual("Product ordered fulfilled", response.json["message"])
        self.assertEqual(200, response.json["status_code"])
        self.assertEqual(12, initial_inventory["1"].stock)
        self.assertEqual(17, initial_inventory["2"].stock)
        self.assertEqual(2, initial_inventory["3"].stock)
        self.assertEqual(8, self.app.config["WAREHOUSE_STORE"]["inventory"]["1"].stock)
        self.assertEqual(9, self.app.config["WAREHOUSE_STORE"]["inventory"]["2"].stock)
        self.assertEqual(1, self.app.config["WAREHOUSE_STORE"]["inventory"]["3"].stock)
