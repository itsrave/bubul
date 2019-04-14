from bu.crawler import LinkCrawler
from bu.crawler import ImageCrawler
from models.link import Link
from models.img import Img
from tqdm import tqdm


class Finder:
    db = None
    url = None

    def start(self):
        pass


class LinkFinder(Finder):
    def __init__(self):
        try:
            mod = Link.select().where(Link.is_done == 0).first()
            mod.is_done = 1
            mod.save()
            self.url = mod.url
        except:
            print('Wystapil blad podczas tworzenia modelu. Plik Finder.py (Brak nowych linkow)')

    def start(self):
        links = None

        try:
            links = LinkCrawler().set_url(self.url).search()
        except:
            print('Wystapil blad podczas szukania linkow.')

        try:
            for link in tqdm(links, desc=self.url):
                count = Link.select().where(Link.url == link).count()

                if count == 0:
                    Link.create(url=link, is_done=0)
        except:
            print('Blad...')


class ImageFinder(Finder):
    def __init__(self, url):
        if url is '':
            try:
                mod = Img.select().where(Img.is_done == 0).first()
                mod.is_done = 1
                mod.save()

                self.url = mod.url
            except:
                pass # print('Wystapil blad podczas tworzenia modelu. Plik Finder.py')
        else:
            self.url = url

    def start(self):
        images = None

        try:
            images = ImageCrawler().set_url(self.url).search()
        except:
            pass # print('Wystapil blad podczas szukania zdjec.')

        try:
            for image in tqdm(images, desc=self.url):
                count = Img.select().where(Img.url == image).count()

                if count == 0:
                    Img.create(url=image, is_done=0)
        except:
            pass # print('Blad...')
