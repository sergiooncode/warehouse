import os

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
    DEBUG = True
    ENV = "local"


config = {"default": LocalConfig}
