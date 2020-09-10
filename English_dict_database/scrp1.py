from bs4 import BeautifulSoup

import requests

from fake_useragent import UserAgent

import selenium

from selenium import webdriver

import pandas as pd
import csv


url = ("https://learnersdictionary.com/3000-words/alpha/")
ua={"UserAgent":'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0'}






lower_alp=[]
page = 1
for alp in range(97 , 97+26):
    url1 = url+chr(alp)
    page = 1
    
    while(page > 0):
        url2 = url1 +"/"+str(page)
        res = requests.get(url2 , headers = ua)

        soup = BeautifulSoup(res.content , features='lxml')

        Next = soup.find('a' , class_="button next")
        print(url2)
       
        page = page+1
        data  = soup.find_all('li')
        
        for i in range(40 , len(data)):
            if str(data[i].find('a').get_text())=='Home':
                break
            y = data[i].find('a').get_text()
            y = y.lstrip()
            y = y.replace(" " , "")
            out = ""
            for i in y:
                if i == '(':
                    break
                out = out+i
            lower_alp.append(out)  
        if Next == None:
            break;             
         


print(lower_alp)
higher_alp = []

for ele in lower_alp:
    higher_alp.append(ele.capitalize())

df = pd.DataFrame(list(zip(lower_alp , higher_alp)) , columns=['Lower' , 'Higher'])

df.to_csv('english_dict.csv')
   


# print(out)


