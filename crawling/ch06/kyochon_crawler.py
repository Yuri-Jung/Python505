# ch06 ex4.py : 커피빈 매장찾기 (동적 웹크롤링)
import time

from bs4 import BeautifulSoup as bs
import urllib.request
import pandas as pd
import datetime

from selenium import webdriver

def kyochon_store(result):

    for sido1 in range(1,18):
        for sido2 in range(1,30):
            kyochon_URL = 'http://www.kyochon.com/shop/domestic.asp?txtsearch=&sido1=%s&sido2=%s' % (sido1, sido2)
            wd = webdriver.Chrome('./WebDriver/chromedriver.exe')
            wd.get(kyochon_URL)
            time.sleep(1)


            html = urllib.request.urlopen(kyochon_URL)
            soupKyochon = bs(html,'html.parser')
            tag_span = soupKyochon.find('span.store_item')

        for store in tag_span.find_all('em'):
            store_name = ('span.store_item>strong').string
            store_address_info= soupKyochon.select ('span.store_item>em')
            store_address= list(store_address_info[0]).string
            # print(store_address_info)
            store_tel = list(store_address_info[2]).string
            result.append([store_name] + [store_address] +[store_tel])

def main():
    result =[]
    kyochon_store(result)
    kyochon_tbl = pd.DataFrame(result, columns=('name', 'address','tel'))
    kyochon_tbl.to_csv("./data/kyochon_store.csv", encoding='cp949', mode='w', index=True)
    print('완료')
    del result[:]

if __name__ =='__main__' :
    main()
