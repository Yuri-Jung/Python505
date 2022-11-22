#ex2.py

aa = []
for i in range(0,4):
    aa.append(0)

sum = 0;
for i in range(0,4):
    aa[i] = int(input(str(i+1) + "번째 숫자 : "))
    sum += aa[i]

print("합계 : %d " % sum)