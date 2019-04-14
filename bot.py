from crawler import Crawler
import os


class Bot:
    def __init__(self, db):
        self.db = db
        self.mod = db.select().where(db.is_done == 0).first()

    def start(self):
        bot = Crawler()
        bot.set_url(self.mod.url)
        links = bot.search()
        link_count = len(links)
        i = 0
        self.mod.is_done = 1
        self.mod.save()
        try:
            for link in links:
                count = self.db.select().where(self.db.url == link).count()
                i += 1
                print('Link: {} {}/{}'.format(self.mod.url, i, link_count))
                if count > 0:
                    continue
                else:
                    self.db.create(url=link, is_done=0)
        except:
            print("Error i chuj jazda dalej")
