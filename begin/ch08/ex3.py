'''
filename : ex3.py
author : JYR
date : 2022.11.28
'''
# 실제 현직에서 추가,수정,삭제한 사람 위에 처럼 남겨놔야한다

ss = input('날짜(연/월/일) 입력 ==> ')

ssList = ss.split('/')
print('입력한 날짜의 10년 후 ==> ', end='')
print(str(int(ssList[0])+10)+'년', end='')
print(ssList[1] + '월',end='')
print(ssList[2] + '일',end='')
# 날짜(연/월/일) 입력 ==> 22/11/28
# 입력한 날짜의 10년 후 ==> 32년11월28일
