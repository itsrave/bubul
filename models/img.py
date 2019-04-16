from peewee import *
from models.db import db


class Img(Model):
    id = IntegerField(primary_key=True)
    imgurl = CharField()

    class Meta:
        database = db
        db_table = 'images'
