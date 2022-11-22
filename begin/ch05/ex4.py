# ex4

# list(리스트)

import random

numbers = []
for num in range(0,10):
    numbers.append(random.randrange(0,10))
#     랜덤 숫자를 배열에 넣어준다

print("생성된 리스트 ", numbers)

for num in range(0,10):
    if num not in numbers:
#        리스트에 해당 숫자가 없으면 실행된다
        print("숫자 %d는 리스트에 없네요" %num)













