
inFp, outFp = None, None
inStr = ""

inFp = open('C:/temp/aa.jpg','rb')
outFp = open('C:/temp/cc.jpg','wb')

while True:
    inStr = inFp.read(1)
    if not inStr:
        break
    outFp.write(inStr)
inFp.close()
outFp.close()
print('---이미지 파일이 정상적으로 복사되었습니다-----')