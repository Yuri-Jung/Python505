# ex3.py

a = 100
result = 0
i = 0

for i in range(1,5):
    result = a + i
    print("%d<<%d = %d" % (a,i,result))

print("-----------------")

for i in range(1,5):
    result = a>>i
    print("%d<<%d = %d" % (a, i, result))