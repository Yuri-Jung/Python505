#ex 9.py

sum, a,b = 0,0,0

while True:
    a = int(input("더 할 첫번째 수를 입력해주세요 : "))
    if a == 0:
        break
    b = int(input("더 할 첫번째 수를 입력해주세요 : "))
    sum = a+b
    print("%d + %d = %d" % (a, b, sum))

print("0을 입력해 반복문을 빠져 나왔습니다")