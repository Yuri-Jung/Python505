# ex2.py : 할리스 매장 정보 크롤링

from bs4 import BeautifulSoup as bs
import urllib.request  # 사이트에 직접 들어가야하기 때문에
import pandas as pd

def hollys_store(result):
    for page in range(1,54): #p173에 59로 잘못 표기
        holly_url = 'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=%d&sido=&gugun=&store=' %page
        #         동적으로 움직이기 위해 pageNo 뒤에 %d를 넣어준다
        # print(holly_url)
        html = urllib.request.urlopen(holly_url)
        soupHollys = bs(html, 'html.parser')
        tag_body = soupHollys.find('tbody')

        # print(tag_body) #엄청나게 출력된다
        for store in tag_body.find_all('tr'):
            store_td = store.find_all_next('td')
            store_name = store_td[1].string
            store_sido = store_td[0].string
            store_address = store_td[3].string
            store_phone = store_td[5].string
            # print('%s %s %s %s' %(store_name,store_sido,store_address,store_phone))
            result.append([store_name] + [store_sido] + [store_address] + [store_phone])


def main():
    result = []
    hollys_store(result)
    holly_tbl = pd.DataFrame(result, columns=('store','sido_gu','address','phone'))
    holly_tbl.to_csv("./data/hollys.csv", encoding='cp949', mode='w', index=True)
    print('완료')
    del result[:]

if __name__ == '__main__' :
    main()
