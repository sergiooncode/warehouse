import os

from config.persistence.settings import MONGO_DB_HOST
from config.persistence.settings import MONGO_DB_NAME

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    @staticmethod
    def init_app(app):
        """
        If some configuration needs to initialize the app in some way use this function
        :param app: Flask app
        :return:
        """
        pass


class LocalConfig(Config):
    MONGODB_SETTINGS = {
        "db": MONGO_DB_NAME,
        "username": "",
        "password": "",
        "host": MONGO_DB_HOST,
        "alias": "default",
    }
    DEBUG = True
    ENV = "local"


class TestConfig(Config):
    MONGODB_SETTINGS = {
        "db": MONGO_DB_NAME,
        "username": "",
        "password": "",
        "host": MONGO_DB_HOST,
        "alias": "default",
    }
    DEBUG = True
    ENV = "test"


config = {
    "test": TestConfig,
    "default": LocalConfig
}
