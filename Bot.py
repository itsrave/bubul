from crawler import Crawler


class Bot:
    crawlers = []
    urls = []
    max_bots = 50

    def __init(self, url):
        self.urls.append = url

    def set_max_bots(self, max):
        self.max_bots = max
        return self

    def start(self):
        i = 0
        urls = []

        if len(self.urls) >= self.max_bots:
            return

        for url in self.urls:
            self.crawlers[i] = Crawler()
            self.crawlers[i].set_url(url)
            urls.extend(self.crawlers[i].search())

        self.urls = urls
