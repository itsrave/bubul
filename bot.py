from crawler import Crawler


class Bot:
    db = 0
    mod = 0

    def __init__(self, db):
        self.db = db
        self.mod = db.select().where(db.is_done == 0).first()

    def start(self):
        bot = Crawler()
        bot.set_url(self.mod.url)
        links = bot.search()

        for link in links:
            count = self.db.select().where(self.db == link).count()

            if count > 0:
                print('Nie wpisuje ' + str(link))
                continue
            else:
                print('Wpisuje ' + str(link))
                self.db.create(url=link, is_done=0)

        self.mod.is_done = 1
        self.mod.save()
