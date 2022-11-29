#  ch12 ex1
# python 특징 :
#   변수 타입이 없고 중괄호 대신 : 사용한다(중괄호 들어가는 위치에 넣어준다)
#   들여쓰기가 아주 중요하다
class Car:
    color =''
    speed = 0
    # self => 객체 자신을 뜻한다
    def upSpeed(self, value):
        self.speed += value
    def downSpeed(self,value):
        self.speed -= value
        if self.speed < 0:
            self.speed = 0

# 여기까지 클래스 생성함

myCar1 = Car()
myCar1.color = 'red'
myCar1.speed = 0

myCar2 = Car()
myCar2.color = 'blue'
myCar2.speed = 0
myCar2.upSpeed(30)

print('자동차1의 색상은 %s이며, 현재 속도는 %dkm입니다' % (myCar1.color, myCar1.speed))
print('자동차2의 색상은 %s이며, 현재 속도는 %dkm입니다' % (myCar2.color, myCar2.speed))