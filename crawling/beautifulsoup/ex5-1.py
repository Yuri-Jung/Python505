

import os,re
import urllib.request as ur
from bs4 import BeautifulSoup as bs

articleA = 'https://n.news.naver.com/mnews/article/015/0004783532?sid=105'
html = ur.urlopen(articleA)
soup = bs(html.read(), 'html.parser')

f = open('./data/links2-1.txt', 'w', encoding='utf-8')

# headline
# headLine = soup.find_all('h2',{'id':'title_area'})[0].text
# print(headLine)

headLine = soup.find_all('h2',class_='media_end_head_headline')[0].text
print(headLine)

# 본문
for i in soup.find_all('div',{'id':'newsct_article'}):
    f.write(i.text + '\n')
f.close()

print('the end')