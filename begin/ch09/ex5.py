#ex5.py
# 더 재밌는 문법
def para_func(*para):
    result = 0
    for num in para:
        result += num
    return result

hap = para_func(10,20)
print('%d' % hap)
hap = para_func(10,20,30)
print('%d' % hap)
hap = para_func(10,20,30,40)
print('%d' % hap)
