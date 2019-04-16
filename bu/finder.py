from bu.crawler import LinkCrawler
from bu.crawler import ImageCrawler
from models.link import Link
from models.img import Img
from tqdm import tqdm


class Finder:
    id = None
    url = None
    title = None
    links = None

    def start(self):
        pass


class LinkFinder(Finder):
    def __init__(self):

        try:
            mod = Link.select().where(Link.is_done == 0).first()

            if mod is None:
                raise Exception('Pusty model')

            mod.is_done = 1
            mod.save()

            self.id = mod.id
            self.url = mod.url
        except Exception as e:
            print(e)

    def start(self):
        links = None

        try:
            data = LinkCrawler().set_url(self.url).search()

            links = data['links']
            title = data['title']

            self._update_title(title)
        except Exception as e:
            print(e)

        try:
            for link in tqdm(links, desc=self.url):
                count = Link.select().where(Link.url == link).count()

                if count == 0:
                    self._create_field(link)
        except Exception as e:
            print(e)
    

    def _update_title(self, title):
        mod = Link.select().where(Link.id == self.id).first()
        mod.title = str(title)
        mod.save()

    @staticmethod
    def _create_field(link):
        mod = Link()

        mod.url = link
        mod.title = ''
        mod.is_done = 0

        mod.save()


class ImageFinder(Finder):
    def __init__(self):
        try:
            mod = Img.select().where(Img.is_done == 0).first()
            mod.is_done = 1
            mod.save()

            self.url = mod.url
        except Exception as e:
            print(e)

    def start(self):
        images = None

        try:
            images = ImageCrawler().set_url(self.url).search()
        except Exception as e:
            print(e)

        try:
            for image in tqdm(images, desc=self.url):
                count = Img.select().where(Img.url == image).count()

                if count == 0:
                    Img.create(url=image, is_done=0)
        except Exception as e:
            print(e)
