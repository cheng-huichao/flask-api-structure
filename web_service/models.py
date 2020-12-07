# -*- coding: utf-8 -*-
# database models
from sqlalchemy.sql import func

from .extensions import db


class Hello(db.Model):
    __tablename__ = 'hello_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    gender = db.Column(db.DateTime, default=func.now(), onupdate=func.now())

    def __repr__(self):
        return '<hello_table {}>'.format(self.name)

