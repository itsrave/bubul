from peewee import *
from models.db import db


class Link(Model):
    id = IntegerField(primary_key=True)
    url = CharField()
    is_done = BooleanField()
    db.connect(reuse_if_open=True)

    class Meta:
        database = db
        db_table = 'urls'
