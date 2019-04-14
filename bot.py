from crawler import Crawler


class Bot:
    def __init__(self, db):
        self.db = db
        link = db.select().where(db.is_done == 0).first()
        self.url = link.url
        self.id = link.id
        self.link = link


    def start(self):
        bot = Crawler()
        bot.set_url(self.url)
        links = bot.search()

        for link in links:
            if str(link) == str(self.db.select().where(self.db.url == link)):
                # break
                print('niewpisuje' + str(link))
            else:
                print('wpisuje' + str(link))
                # self.db.create(url=link, is_done=0)
        # self.link.is_done = 1
        # self.link.save()
