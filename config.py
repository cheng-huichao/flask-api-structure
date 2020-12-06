# -*- coding: utf-8 -*-
import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or "!8DZ56!JQd9s0HHKjhsdP3,ZqWQR%fn/-z'MYgB;W4"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfigmap(Config):
    """
    Development Config
    """

    SQLALCHEMY_DATABASE_URI = "sqlite:///dev.db"


class ProductionConfigmap(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///dev.db"
    # sqlite: win use [sqlite://] linux & Mac use [sqlite:///]


config_map = {
    'default': DevelopmentConfigmap,
    'development': DevelopmentConfigmap,
    'production': ProductionConfigmap,
}
