from db import DataBase
from crawler import Crawler
from bot import Bot


bot = Bot(DataBase)
bot.start()
# bot = Crawler()
# bot.set_url('http://www.onet.pl')
# links = bot.search()
# print(links)
# for link in links:
#     Url.create(url=link, is_done=0)
