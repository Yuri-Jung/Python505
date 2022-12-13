# ch06 ex4.py : 커피빈 매장찾기 (동적 웹크롤링)
# import time

# from bs4 import BeautifulSoup as bs
# import urllib.request
# import pandas as pd
# import datetime
#
# from selenium import webdriver
#
# def pelicana_store(result):
#     for page in range(1,110):
#         pelicana_URL = 'http://www.pelicana.co.kr/store/stroe_search.html?&branch_name=&gu=&si=&page=%s' %page
#         html = urllib.request.urlopen(pelicana_URL)
#         soupPelicana = bs(html,'html.parser')
#         tag_body = soupPelicana.find('tbody')
#
#         for store in tag_body.find_all('tr'):
#             store_td = store.find_all_next('td')
#             store_name = store_td[0].string
#             store_address = store_td[1].string
#             store_tel = store_td[2].string
#             result.append([store_name] + [store_address] +[store_tel])
#         # print('%s %s %s' %(store_name,store_address,store_tel))
# def main():
#     result =[]
#     pelicana_store(result)
#     pelicana_tbl = pd.DataFrame(result, columns=('name', 'address','tel'))
#     pelicana_tbl.to_csv("./data/pelicana_store.csv", encoding='cp949', mode='w', index=True)
#     print('완료')
#     del result[:]
#
# if __name__ =='__main__' :
#     main()


# ////////////////////////
# 선생님코드
# pelicana_crawler.py

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

def getPelicanaAddress(result):
    for page_idx in count():
        # print(page_idx)
        url='http://www.pelicana.co.kr/store/stroe_search.html?&branch_name=&gu=&si=&page=%s' % str(page_idx+1)
        # print('[Pelicana Page] : [%s]' % str(page_idx+1))

        rcv_data = get_request_url(url)
        soupData = BeautifulSoup(rcv_data,'html.parser')
        store_table = soupData.find('table', attrs={'class':'table mt20'})
        tbody = store_table.find('tbody')
        # print(tbody)
        bEnd = True
        for store_tr in tbody.findAll('tr'):
            bEnd = False
            tr_tag = list(store_tr.strings)
            # print(tr_tag[0])
            # print(tr_tag[1])
            # print(tr_tag[2])
            # print(tr_tag[3])

            store_name = tr_tag[1]
            store_address = tr_tag[3]
            store_sido_gu = store_address.split()[0:2]
            result.append([store_name]+ store_sido_gu + [store_address])
        if(bEnd == True):
            print(result[0])
            print('--데이터 수 : %d' % len(result))
            return
    return



def cswin_pericana():
    result = []
    print('Pelicana Address Crawling Start')
    getPelicanaAddress(result);
    pericana_table = pd.DataFrame(result, columns=('store', 'sido', 'gungu', 'store_address'))
    pericana_table.to_csv('./data/pericana.csv', encoding='cp949', mode='w', index=True)
    del result[:]
    print('finish')

if __name__ == '__main__':
    cswin_pericana()


















