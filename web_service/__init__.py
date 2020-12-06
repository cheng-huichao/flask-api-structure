# -*- coding: utf-8 -*-
from flask import Flask
from flask_cors import CORS

from config import config_map
from .api_bp import api_bp
from .extensions import db, migrate


def create_app(config_name='development'):
    app = Flask(__name__)
    # CORS(app)
    CORS(app, resources={r"*": {"origins": "*"}})

    # load configuration
    app.config.from_object(config_map[config_name])
    config_map[config_name].init_app(app)

    # logging config
    # [%(asctime)s] p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s','%m-%d %H:%M:%S
    # logging.basicConfig(filename='app.log', level=logging.DEBUG,
    #                     format='[%(asctime)s] p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s')
    # initial extensions
    # mail.init_app(app)
    migrate.init_app(app=app, db=db)
    db.init_app(app)

    # register blueprint
    app.register_blueprint(api_bp)


    return app
