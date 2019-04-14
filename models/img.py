from peewee import *
from models.db import db


class Img(Model):
    id = IntegerField(primary_key=True)
    url = CharField()
    is_done = BooleanField()
    db.connect()

    class Meta:
        database = db
        db_table = 'imgs'
