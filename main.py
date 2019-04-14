from crawler import Crawler
bot = Crawler()
bot.set_url('https://www.wp.pl')
links = bot.search()
for link in links:
    print(link)
    print('')
