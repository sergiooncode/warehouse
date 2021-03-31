import os

from flask import Flask

from bin.cli.seed_data import load_seed_data
from config import config

from src.infrastructure.controller.base import api


def create_app(config_name=os.getenv("ENVIRONMENT") or "default"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    with app.app_context():
        load_seed_data()

        api.init_app(app)

    return app


app = create_app()
