from peewee import *

db = MySQLDatabase('bubul', user='root1', passwd='123456')


class DataBase(Model):
    id = IntegerField(primary_key=True)
    url = CharField()
    is_done = BooleanField()
    db.connect()

    class Meta:
        database = db
        db_table = 'urls'
