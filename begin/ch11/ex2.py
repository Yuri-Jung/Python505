import os

inFp = None
fName, inList, inStr = '',[],''

fName = input('파일명을 입력하세요')

# inFp = open('C:/temp/data1.txt','r',encoding="utf-8") 파일명 때문에 가져옴

if os.path.exists(fName):
    inFp = open(fName, 'r', encoding='utf-8')
    inList = inFp.readlines()
    for inStr in inList:
        print(inStr, end='')
    inFp.close()
else:
    print('%s 파일이 없습니다' % fName)