# ex3.py

# 1~100 사이의 값 들 중 짝수는 aa, 홀수는 bb에 저장하시오
aa = []
bb = []


for i in range(0,102,2):
    aa.append(i)
    # print(aa[i + 2]) #범위를 벗어나게 된다.
for i in range(1,101,2):
    bb.append(i)
print(aa)
print(bb)