from bs4 import BeautifulSoup

import requests

from fake_useragent import FakeUserAgent

import selenium

from selenium import webdriver

driver = webdriver.Firefox()

url = ("https://learnersdictionary.com/3000-words/alpha/b/")
page = 2
url = url + str(page)

driver.get(url)

html = driver.page_source

soup = BeautifulSoup(html , features='lxml')

data  = soup.find_all('li')
driver.close()

for i , val in enumerate(data):
    print(i , val)
    if str(data[i].find('a').get_text())=='Home':
        break
    





