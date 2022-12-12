# ch06 ex3.py : chromedriver.exe을 지정한 위치에 저장

from selenium import webdriver
wd = webdriver.Chrome('./WebDriver/chromedriver.exe')

wd.get('https://www.hanbit.co.kr/') #한빛미디어 껐다 켜짐


