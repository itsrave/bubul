from crawler import Crawler
from tqdm import tqdm


class Bot:
    def __init__(self, db):
        self.db = db
        self.mod = db.select().where(db.is_done == 0).first()

    def start(self):
        bot = Crawler()
        bot.set_url(self.mod.url)
        self.mod.is_done = 1
        self.mod.save()
        try:
            links = bot.search()
        except:
            pass
        try:
            for link in tqdm(links, desc=self.mod.url):
                count = self.db.select().where(self.db.url == link).count()
                if count > 0:
                    continue
                else:
                    self.db.create(url=link, is_done=0)
        except:
            print("Error i chuj jazda dalej")

    def start_img(self):
        bot = Crawler()
        bot.set_url(self.mod_img.url)
        self.mod_img.img_is_done = 1
        self.mod_img.save()
        try:
            links = bot.search_images()
        except:
            pass
        try:
            for link in tqdm(links):
                self.db.create(imgurl=link)
        except:
            print("Error i chuj jazda dalej")
