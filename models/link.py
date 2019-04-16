from peewee import *
from models.db import db


class Link(Model):
    id = IntegerField(primary_key=True)
    url = CharField()
    is_done = BooleanField()
    title = CharField()


    class Meta:
        database = db
        db_table = 'urls'
