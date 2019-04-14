from bs4 import BeautifulSoup
import requests


class Crawler:
    url = ''
    found_urls = []
    found_imgs = []
    ignored = 0

    def get_url(self) -> str:
        return self.url

    def set_url(self, url):
        self.url = url
        return self

    def get_found_urls(self) -> list:
        return self.found_urls

    def search(self) -> list:
        r = requests.get(self.url)
        soup = BeautifulSoup(r.content, 'html.parser')
        links = soup.find_all('a')

        for link in links:
            try:
                if str(link['href']).startswith('http') is True:
                    self.found_urls.append(link['href'])
                else:
                    pass
            except:
                self.ignored += 1

        return self.found_urls

    def search_images(self) -> list:
        r = requests.get(self.url)
        soup = BeautifulSoup(r.content, 'html.parser')
        links = soup.find_all('img')
        for link in links:
            try:
                self.found_imgs.append(link['src'])
            except:
                self.ignored += 1
        return self.found_imgs
