from bs4 import BeautifulSoup
import requests


class Crawler:
    search_link = ''
    ignored = 0

    def search(self) -> dict:
        pass

    def set_url(self, url):
        self.search_link = url
        return self

    def get_url(self) -> str:
        return self.search_link

    def get_ignored(self) -> int:
        return self.ignored


class LinkCrawler(Crawler):
    found_urls = []

    def get_founded_urls(self) -> list:
        return self.found_urls

    def search(self):
        links = None
        title = None

        r = requests.get(self.search_link)
        soup = BeautifulSoup(r.content, 'html.parser')

        try:
            links = soup.find_all('a')
            title = soup.find('title').text
        except Exception as e:
            print(e)

        for link in links:
            if str(link['href']).startswith('http') is True:
                self.found_urls.append(link['href'])

        return {
            'links': self.found_urls,
            'title': title
        }


class ImageCrawler(Crawler):
    found_imgs = []

    def get_founded_imgs(self) -> list:
        return self.found_imgs

    def search(self):
        r = requests.get(self.search_link)
        soup = BeautifulSoup(r.content, 'html.parser')
        links = soup.find_all('img')

        for link in links:
            try:
                self.found_imgs.append(link['src'])
            except Exception as e:
                self.ignored += 1
                print(e)

        return {
            'links': self.found_imgs
        }
