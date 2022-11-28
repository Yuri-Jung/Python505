
ss = '파이썬 짱'

sslen = len(ss)
for i in range(0,sslen):
    print(ss[i] + '$', end='')
    # 파$이$썬$ $짱$

inStr,outStr = ", " #띄워쓰기 조심!!
count, i = 0,0
inStr = input("문자열을 입력하세요 : ")
count = len(inStr)

for i in range(0,count):
    outStr += inStr[count - (i+1)]
print('내용을 거꾸로 출력 --> %s' % outStr)
# 안뇽하세요
# 내용을 거꾸로 출력 -->  요세하뇽안












