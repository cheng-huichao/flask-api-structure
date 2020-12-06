# -*- coding: utf-8 -*-
from flask import Blueprint

api_bp = Blueprint('api_bp', __name__, url_prefix='/api')

from . import api
