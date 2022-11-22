#ex4.py

# i,dan,dan2,j =0,0
# dan = int(input("단을 입력하세요 : "))
# for i in range(1,10,1):
#     print("%d x %d = %2d" % (dan,i,dan*i))
    # %2d : 공백을 뜻함 커질 수록 공백 커짐


dan = int(input("단 선택해주세요"))

for i in range(dan,10,1):
    print("%d단" % (i))
    for j in range(1,10,1):
        print(" %d x %d = %d" % (i,j,i*j))

# for i in range(2,10,1):
#     print("# %d단 # " % i, end="")
# print("")
#
# for i in range(1,10,1):
#     for j in range(2,10,1):
#         print("%d x %d = %2d\t" % (j,i,j*i),end="")









