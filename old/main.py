from db import *
from crawler import Crawler
from bot import Bot

while True:
    bot = Bot(ImgDataBase)
    bot.start_img()
