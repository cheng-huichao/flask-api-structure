# -*- coding: utf-8 -*-
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from web_service.utils.my_logger import get_logger

db = SQLAlchemy()
migrate = Migrate()
my_logger = get_logger('web_service')
