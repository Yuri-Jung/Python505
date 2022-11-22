#ex 10
sum = 0

for i in range(1,101):
    if i % 3 == 0:
        continue
    sum += i

print("1~100의 합계 (3의 배수 제외) : %d" %sum)

