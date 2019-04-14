from db import DataBase


class Search:
    def __init__(self, text, db):
        self.text = text
        self.db = db

    def search(self) -> list:
        urls = self.db.select().where(self.db.url.contains(self.text))
        return urls
