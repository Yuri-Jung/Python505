# ch06 ex4.py : 커피빈 매장찾기 (동적 웹크롤링)
import time

from bs4 import BeautifulSoup as bs
import urllib.request
import pandas as pd
import datetime

from selenium import webdriver

def pelicana_store(result):
    for page in range(1,110):
        pelicana_URL = 'http://www.pelicana.co.kr/store/stroe_search.html?&branch_name=&gu=&si=&page=%s' %page
        html = urllib.request.urlopen(pelicana_URL)
        soupPelicana = bs(html,'html.parser')
        tag_body = soupPelicana.find('tbody')

        for store in tag_body.find_all('tr'):
            store_td = store.find_all_next('td')
            store_name = store_td[0].string
            store_address = store_td[1].string
            store_tel = store_td[2].string
            result.append([store_name] + [store_address] +[store_tel])
        # print('%s %s %s' %(store_name,store_address,store_tel))
def main():
    result =[]
    pelicana_store(result)
    pelicana_tbl = pd.DataFrame(result, columns=('name', 'address','tel'))
    pelicana_tbl.to_csv("./data/pelicana_store.csv", encoding='cp949', mode='w', index=True)
    print('완료')
    del result[:]

if __name__ =='__main__' :
    main()

