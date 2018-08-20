from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


class Title(db.Model):
    __tablename__ = 'titles'
    title_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    #creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    #done = db.Column(db.Boolean, unique=False, default=False)
  

    def __init__(self, title_id,title, description):
        self.title_id = title_id
        self.title = title
        self.description = description

       

        



class TitleSchema(ma.Schema):
    title_id = fields.Integer(dump_only=True)
    title = fields.String(required=False, validate=validate.Length(1))
    #creation_date = fields.DateTime()
    description = fields.String(required=False, validate=validate.Length(1))
    #done = fields.Boolean(required=True)
