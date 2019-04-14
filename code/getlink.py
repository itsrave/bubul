from bs4 import BeautifulSoup
import requests
import os
path = os.getcwd()


def getlinks(address):
    r = requests.get("http://www." + address)
    soup = BeautifulSoup(r.content, 'html.parser')
    links = soup.find_all('a')
    open(path + '/data/' + address, 'w').close()
    for link in links:
        if str(link['href']).startswith("/") is True:
            with open(path + '/data/' + address, 'a') as f:
                f.write(address + link['href'] + "\n")
        elif str(link['href']).startswith(str(address)) is True:
            with open(path + '/data/' + address, 'a') as f:
                f.write(link['href'] + "\n")
        else:
            pass
    return links


def lel():
    with open("pages.txt", "r") as f:
        links = f.read().splitlines()
    for i in links:
        getlinks(i)


getlinks('akita-u.ac.jp')