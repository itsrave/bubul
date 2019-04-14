from crawler import Crawler
import peewee
from peewee import *

db = MySQLDatabase('bubul', user='root1', passwd='123456')
print(db.)
# class Book(peewee.Model):
#     author = peewee.CharField()
#     title = peewee.TextField()
#
#     class Meta:
#         database = db
#
# Book.create_table()
# book = Book(author="me", title='Peewee is cool')
# book.save()
# for book in Book.filter(author="me"):
#     print book.title

bot = Crawler()
bot.set_url('https://www.wp.pl')
links = bot.search()
for link in links:
    print(link)
    print('')
