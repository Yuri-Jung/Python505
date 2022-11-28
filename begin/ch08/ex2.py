'''
파일명 : ex2.py
개발자 : JYR
'''

# ss = input('입력 문자열 ==> ')
# print('출력 문자열 ==> ', end='')
#
# if ss.startswith('(')==False:
#     print('(', end='')
#
# print(ss,end='')

# 입력 문자열 ==> 무궁화꽃이 피었습니다
# 출력 문자열 ==> (무궁화꽃이 피었습니다
#
# if ss.endswith(')')==False:
#     print(')', end='')

# 입력 문자열 ==> 무궁화꽃이 피었습니다
# 출력 문자열 ==> (무궁화꽃이 피었습니다)

inStr = '     한글 Python 프로그래밍      '
outStr = inStr.replace(" ","")

for i in range(0,len(inStr)):
    if inStr[i] != '':
        outStr += inStr[i]


print("원래 문자열 ==> " + '['+inStr+']')
print("공백 삭제 문자열 ==> " +'[' + outStr + ']')

# i를 $로 출력하기
inStr = 'Live as if you will die today.'

print(inStr.replace('i','$'))
# L$ve as $f you w$ll d$e today.






