
# nvCrawler_blog.py : 네이버 블로그 크롤링

import os,sys
import urllib.request
import datetime, time
import json

client_id ="TY0XEecDCcFWi33nL8uC"
client_secret="5U0WY4HGc7"

# [CODE 1]
def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None


# [CODE 2]
def getNaverSearch(node, srcText, start, display):
    base = "https://openapi.naver.com/v1/search"
    node = "/%s.json" % node
    parameters = "?query=%s&start=%s&display=%s" % (urllib.parse.quote(srcText), start, display)

    url = base + node + parameters
    responseDecode = getRequestUrl(url)  # [CODE 1]

    if (responseDecode == None):
        return None
    else:
        return json.loads(responseDecode)

# [CODE 3]
def getPostData(post, jsonResult, cnt):
    title = post['title']
    link = post['link']
    description = post['description']
    bloggername = post['bloggername']
    pDate = post['postdate']

    jsonResult.append({'cnt': cnt, 'title': title, 'description': description,
                       'link': link, 'pDate': pDate, 'blogger': bloggername})

# [CODE 4]
def main():
    node = 'blog'
    srcText = input('검색어를 입력하세요 : ')
    cnt = 0
    jsonResult = []

    jsonResponse = getNaverSearch(node, srcText, 1, 100) #[CODE 2]
    total = jsonResponse['total']

    while((jsonResponse != None) and (jsonResponse['display'] !=0)):
        for post in jsonResponse['items']:
            cnt += 1
            getPostData(post,jsonResult,cnt) #[CODE 3 ]

        start = jsonResponse['start'] + jsonResponse['display']
        jsonResponse = getNaverSearch(node, srcText, start, 100) #[CODE 2]

    print('전체 검색 : %d건' %total)
    with open('./data/%s_naver_%s.json' % (srcText,node),'w',encoding='utf-8') as outfile :
        jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        # indent : 들여쓰기

        outfile.write(jsonFile)
    print('가져온 데이터 : %d건' %cnt)
    print('%s_naver_%s.json SAVED' % (srcText,node))

if __name__ == '__main__' :
    main()





















