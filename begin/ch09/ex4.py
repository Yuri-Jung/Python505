
def multi(v1,v2):
    reList = []
    res1 = v1 + v2
    res2 = v1 - v2
    reList.append(res1)
    reList.append(res2)
    return reList

myList = []
hap, sub = 0,0

myList = multi(100,200)
hap = myList[0]
sub = myList[1]

print('multi()에서 돌려준 값 ==> %d, %d' % (hap,sub))

# 재밌는 문법
def para_func(v1,v2,v3 = 0):
    result = 0
    result = v1+v2+v3
    return result
hap = 0
hap = para_func(10,20)
print("매개변수 2개의 계산결과 ==> %d" % hap)
hap = para_func(10,20,30)
print("매개변수 3개의 계산결과 ==> %d" % hap)

