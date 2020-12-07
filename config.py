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
    # ** sqlite **#
    # SQLALCHEMY_DATABASE_URI = "sqlite:///dev.db"

    # ** mysql **#
    # SQLALCHEMY_DATABASE_URI = "mysql://<username>:<password>@<servername>/<dbname>"

    # ** postgresql **#
    # SQLALCHEMY_DATABASE_URI = "postgresql://<username>:<password>@<servername>/<dbname>"

    # ** mssql **#
    ## pip install pymssql

    SQLALCHEMY_DATABASE_URI = "mssql+pymssql://<username>:<password>@<servername>:<port>/<dbname>"

    # 注意 ***** 数据table会被删除 ☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️ 如果model 里面没有定义


class ProductionConfigmap(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///dev.db"
    # sqlite: win use [sqlite://] linux & Mac use [sqlite:///]


config_map = {
    'default': DevelopmentConfigmap,
    'development': DevelopmentConfigmap,
    'production': ProductionConfigmap,
}
