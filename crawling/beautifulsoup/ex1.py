# pip install beautifulsoup4

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.naver.com')
obj = BeautifulSoup(html,'html.parser')

# print(obj)

# for meta in obj.head.find_all('meta'):
#     print(meta.get('content'))

# print(obj.head.find('meta', {'name' : 'description'}).get('content'))
# 네이버 메인에서 다양한 정보와 유용한 컨텐츠를 만나 보세요

#  a 태그 다 찾아와라
for link in obj.find_all('a'):
    print(link.text.strip(), link.get('href'))














