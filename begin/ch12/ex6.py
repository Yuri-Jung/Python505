# ch12 ex6
# 다양한 메서드들
class Line:
    length = 0

    def __init__(self, length):
        self.length = length
        print(self.length, '길이의 선이 생성되었습니다')

    def __del__(self):
        print(self.length, '길이의 선이 제거되었습니다')

    # print 호출 시 사용됨
    def __repr__(self):
        return '선의 길이 : ' + str(self.length)

    # 객체와 객체가 더해졌을 때
    def __add__(self, other):
        return self.length + other.length

    # less than 비교연산자
    def __lt__(self, other):
        return self.length < other.length

    # equal
    def __eq__(self, other):
        return self.length == other.length

myLine1 = Line(200)
myLine2 = Line(200)

print(myLine1)
# print(myLine2)

# 더하기만 하더라도 add가 호출된다
print('두 선의 길이 합계' , myLine1 + myLine2)
# 두 선의 길이 합계 300

if myLine1 < myLine2:
    print('myLine2가 더 길네요')
elif myLine1 == myLine2:
    print('myLine1과 myLine2의 길이가 같네요')
else:
    print('모르겠습니다')

del(myLine1)
# del(myLine2)