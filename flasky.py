# -*- coding: utf-8 -*-
from flask_migrate import Migrate

from web_service import create_app, db

app = create_app('development')

# @app.shell_context_processor
# def make_shell_context():
#     """
#     go in flask shell to use the instance
#     :return:
#     """
#     return dict(db=db, APIData=api_store)
#

@app.route('/')
def index():
    html = """
        <a href='/api/'>API index</a>
    """
    return html
