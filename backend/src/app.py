import os

from config import config
from flask import Flask
from src.infrastructure.controller.base import api

from src.infrastructure.persistence.mongoengine.model import db

from bin.cli.seed_data import load_mongo_seed_data


def create_app(config_name=os.getenv("ENVIRONMENT") or "default"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    with app.app_context():
        # Mongoengine setup
        db.init_app(app)
        load_mongo_seed_data()

        api.init_app(app)

    return app


app = create_app()
