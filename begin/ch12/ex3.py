class Car:
    color =''
    speed = 0


    def __init__(self,var1,var2):
        self.speed = var1
        self.color = var2

    # self => 객체 자신을 뜻한다
    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self,value):
        self.speed -= value
        if self.speed < 0:
            self.speed = 0

myCar3 = Car(50, 'orange')
print('자동차3의 색상은 %s이며, 현재 속도는 %dkm입니다' % (myCar3.color, myCar3.speed))