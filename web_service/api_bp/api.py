# -*- coding: utf-8 -*-
from flask import jsonify

from . import api_bp

from web_service.models import Hello

@api_bp.route("/", methods=['get', ])
def hello():
    return jsonify({"Hello": "world!"})
