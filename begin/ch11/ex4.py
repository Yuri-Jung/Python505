# ch11 ex4 파일복사

inFp, outFp = None, None
inStr = ''

inFp = open('C:/temp/data1.txt','r',encoding="utf-8")
outFp = open('C:/temp/data5.txt','w',encoding="utf-8")

inList = inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print('---복사완료---')