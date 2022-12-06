# ex1.py

import numpy as np

# print(np.__version__)

ar1 = np.array([1,2,3,4,5])
# print(ar1)
# print(type(ar1))

ar2 = np.array([[1,2,3,4,5],[6,7,8,9,10]]) #크기가 같아야 하나봄
# print(ar2)

ar3 = np.arange(1,11,2) #1에서 11까지 증가값이 2(홀수)
# print(ar3)

ar4 = np.arange(1,31,3) # 31포함 안됨
# print(ar4)

ar5 = np.array([1,2,3,4,5,6]).reshape((3,2)) #2개씩 3줄로 출력(3행 2열)
# print(ar5)

ar6 = np.zeros((2,3))
# print(ar6)
# [[0. 0. 0.]
#  [0. 0. 0.]]  0으로 2열 3행

ar7 = np.array([[10,20,30],[40,50,60]])
ar8 = ar7[0:2,0:2]
# print(ar8)
# [[10 20] [index번호 : 갯수] 디폴트가 0. [:5] 5개를 가져온다
#  [40 50]]

ar9 = ar7[0:]
ar10 = ar7[0,:]
# print(ar9)
# print("--------------------")
# print(ar10)

# ar9 = ar7[0:]
# [[10 20 30]
#  [40 50 60]]

# ar10 = ar7[0,:]
# [10 20 30]
# 두 개의 차이가 존재한다

ar11 = np.array(([1,2,3,4,5]))
ar12 = ar11 + 10
print(ar12)
# [11 12 13 14 15]  요소들 마다 값이 더해진다

ar13 = ar11 +ar12
print(ar13)
# [12 14 16 18 20]
# 세로로 값이 더해짐

ar14 = ar13 * 2
print(ar14)
# [24 28 32 36 40] // [12 14 16 18 20]에서 각 항목이 *2됨











