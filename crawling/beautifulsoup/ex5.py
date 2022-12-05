
# ex5.py

import os,re
import urllib.request as ur
from bs4 import BeautifulSoup as bs

article1 = 'https://v.daum.net/v/20200427090630709'
html = ur.urlopen(article1)
soup = bs(html.read(),'html.parser')

# 파일 안에 데이터 가져오기
f= open('./data/links.txt', 'w', encoding='utf-8')

# headline 출력
headLine = soup.find_all('h3', {'class':'tit_view'})[0].text
print(headLine)

# 특정기사 본문 저장하기
for i in soup.find_all('p'):
    f.write(i.text + '\n')
f.close()
