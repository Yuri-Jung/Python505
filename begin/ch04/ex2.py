#ex2.py
a = ord('a')
# print(a) #a = 65
a = ord('A') # 65
mask = 0x0F #15

# print(mark)

# ord는 유니코드로 변환해주는 함수

# %x - 16진수
# %o - 8진수
print("%x & %x = %x" %(a, mask, a & mask)) # 41 & f = 1
print("%X & %X = %X" %(a, mask, a | mask)) # 41 & F = 4F

mask = ord('a') - ord('A')
# print(mask) # 32

b = a^mask #%c는 글자
print("%c^%d = %c" % (a,mask,b)) # 32 (값이 다르면0 같으면1)
a = b^mask
print("%c^%d = %c" % (b,mask,a))







