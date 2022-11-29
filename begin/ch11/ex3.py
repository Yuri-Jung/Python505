outFp = None
outStr = ''

outFp = open('C:/temp/data2.txt','w') # 파일이 w이기 때문에 만들어짐

while True:
    outStr = input('내용 입력 : ')
    if outStr != '':
        outFp.write(outStr + '\n')
    else:
        break
outFp.close()
print('파일이 정상적으로 써졌다')
# 마지막에 아무것도 치지 않아야 저장된다