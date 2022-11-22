#ex2.py

# 500과 1000 사이의 있는 홀수의 합계
sum = 0
for i in range(500,1001):
    if(i%2 != 0):
        sum = sum+i
print("sum는 %d" %sum)

sum = 0
for i in range(501,1001,2):
    sum = sum+i
print("sum는 %d" %sum)







