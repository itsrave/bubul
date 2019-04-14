from bs4 import BeautifulSoup
import requests
import re
import csvv


def getschools():
    link = "https://en.wikipedia.org/wiki/List_of_national_universities_in_Japan"
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'html.parser')
    schools = soup.find('ul').find_all('a')
    for i in schools:
        print(i.text)
    return schools


def getschoolslinks():
    link = "https://en.wikipedia.org/wiki/List_of_national_universities_in_Japan"
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'html.parser')
    schools = soup.find('ul').find_all('a')
    return schools


def getschoolspage(schools):
    for i in schools:
        link = "https://en.wikipedia.org" + i['href']
        r = requests.get(link)
        soup = BeautifulSoup(r.content, 'html.parser')
        pages = []
        try:
            page = soup.find('span', id="External_links").find_next("a", class_="external text")
            print(page['href'])
            pages.append(page['href'])
        except AttributeError:
            print("No webpage")
    return pages


print(getschoolspage(getschoolslinks()))
