from peewee import *
from models.db import db


class Img(Model):
    id = IntegerField(primary_key=True)
    imgurl = CharField()
    db.connect(reuse_if_open=True)

    class Meta:
        database = db
        db_table = 'images'
