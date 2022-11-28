#ex6.py

import random
def getNumber():
    return random.randrange(1,46) #1~45 범위
lotto = []
num = 0

print('*** 로또 추첨을 시작합니다 ***\n')
while True:
    num = getNumber()
    if lotto.count(num) == 0:
        lotto.append(num)
        # lotto 에 들어가있는 'n'의 개수
    # 리스트 안에는 반복된 값이 들어갈 수 있다.
    # count로 반복된 값을 없앨 수 있다

    if len(lotto) >= 6:
        break

print('추천된 로또 번호 ==> ', end='')
lotto.sort()
for i in range(0,6):
    print('%d' % lotto[i], end=', ')