# # ch06 ex4.py : 커피빈 매장찾기 (동적 웹크롤링)
# import time
#
# from bs4 import BeautifulSoup as bs
# import urllib.request
# import pandas as pd
# import datetime
#
# from selenium import webdriver
#
# def kyochon_store(result):
#
#     wd =webdriver.Chrome('./WebDriver/chromedriver.exe')
#     for sido1 in range(1,20):
#         for sido2 in range(1,30):
#             kyochon_URL = 'http://www.kyochon.com/shop/domestic.asp?txtsearch=&sido1=%s&sido2=%s' % (sido1, sido2)
#             wd.get(kyochon_URL)
#             time.sleep(1)
#             try:
#                 wd.execute_script('store_item')
#                 html = wd.page_source
#                 soupKyochon = bs(html,'html.parser')
#                 ul_tag = soupKyochon.select('div.shopSchList>ul')
#                 for store_data in ul_tag.findAll('a'):
#                     store_name = store_data.find('strong').get_text()
#                     store_address = store_data.find('em').get_text().strip().split('\r')[0]
#                     store_sido_gu = store_address.split()[:2]
#                     result.append([store_name] + store_sido_gu + [store_address])
#                     print(store_name,store_address,store_sido_gu)
#             except:
#                 continue
#         return
# def main():
#     result =[]
#     kyochon_store(result)
#     kyochon_tbl = pd.DataFrame(result, columns=('name', 'address','tel'))
#     # kyochon_tbl.to_csv("./data/kyochon_store.csv", encoding='cp949', mode='w', index=True)
#     print('완료')
#     del result[:]
#
# if __name__ =='__main__' :
#     main()


# ////////////////////////////////////////////////////////
# 선생님 코드

#kyochon_crawler.py : 매장 정보 크롤링

import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import datetime
from itertools import count

import ssl # 접속 보안 허용

def get_request_url(url,enc ='utf-8'):
    req = urllib.request.Request(url)
    try:
        # [SSL: CERTIFICATE_VERIFY_FAILED] 에러 뜰때
        ssl._create_default_https_context = ssl._create_unverified_context  # 접속보안 허용
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            try:
                rcv = response.read()
                # 한글로 변환
                ret = rcv.decode(enc)
            except UnicodeDecodeError:
                # replace : 에러 발생시 ?로 변환이 된다
                ret = rcv.decode(enc,'replace')
            return ret

    #         정상적으로 응답할 경우 200번이 날라온다
    except Exception as e:
        print(e)
        print('[%s]Error for URL : %s' % (datetime.datetime.now(),url))
        return None

def getKyochonAddress(sido1, result):
    for sido2 in count():
        url = 'http://www.kyochon.com/shop/domestic.asp?txtsearch=&sido1=%s&sido2=%s' % (str(sido1),str(sido2))
        # print(url)
        try:
            rcv_data = get_request_url(url)
            soupData = BeautifulSoup(rcv_data,'html.parser')
            ul_tag = soupData.find('ul',attrs={'class':'list'})
            # print(ul_tag)

            for store_data in ul_tag.find_all('a', href=True):
                store_name = store_data.find('strong').get_text();
                # print(store_name)
                store_address = store_data.find('em').get_text().strip().split('\r')[0]
                store_sido_gu = store_address.split()[0:2]
                # print(store_sido_gu)
                result.append([store_name] + store_sido_gu + [store_address])
        except:
            break
    return

def cswin_Kyochon():
    result = []
    print('Kyochon Address Crawling Start')
    for sido1 in range (1,18):
        getKyochonAddress(sido1,result);
    kyochon_table = pd.DataFrame(result, columns=('store', 'sido', 'gungu', 'store_address'))
    kyochon_table.to_csv('./data/kyochon.csv', encoding='cp949',mode='w', index=True)
    del result[:]
    print('finish')


if __name__ == '__main__':
    cswin_Kyochon()












