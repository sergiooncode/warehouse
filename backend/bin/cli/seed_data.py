import json
import sys

from flask import current_app

from src.domain.model.article_inventory import ArticleInventory
from src.domain.model.canonical_article import CanonicalArticle
from src.domain.model.canonical_product import CanonicalProduct
from src.infrastructure.persistence.inmemory.model import session


def load_seed_data():
    print("Loading seed data...", file=sys.stderr)

    with open("resources/inventory.json") as json_file:
        inventory_data = json.load(json_file)

        for article in inventory_data["inventory"]:
            if not session["inventory"]:
                session["inventory"] = {
                    article["art_id"]: ArticleInventory(
                        article_id=article["art_id"],
                        name=article["name"],
                        stock=int(article["stock"]),
                    )
                }
            else:
                session["inventory"][article["art_id"]] = ArticleInventory(
                    article_id=article["art_id"],
                    name=article["name"],
                    stock=int(article["stock"]),
                )

    with open("resources/products.json") as json_file:
        canonical_product_data = json.load(json_file)

        for product in canonical_product_data["products"]:
            containing_articles = []
            for containing_article in product["contain_articles"]:
                containing_articles.append(
                    CanonicalArticle(
                        article_id=containing_article["art_id"],
                        needed_amount=int(containing_article["amount_of"]),
                    )
                )
            if not session["products"]:
                session["products"] = {
                    product["name"]: CanonicalProduct(
                        name=product["name"],
                        price=100,
                        containing_articles=containing_articles,
                    )
                }
            else:
                session["products"][product["name"]] = CanonicalProduct(
                    name=product["name"],
                    price=100,
                    containing_articles=containing_articles,
                )

    current_app.config["WAREHOUSE_STORE"] = session
