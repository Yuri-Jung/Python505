import turtle
import random
# 함수 선언부분
def screenLeftClick(x,y):
    global r,g,b
    # global 붙이면 전역변수가 된다
    turtle.pencolor((r,g,b))
    turtle.pendown()
    turtle.goto(x,y)

def screenRightClick(x,y):
    turtle.penup()
    turtle.goto(x,y)

def screenMidClick(x,y):
    global r,g,b
    tSize = random.randrange(1, 10)
    turtle.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()

pSize = 10
r,g,b = 0.0,0.0,0.0
turtle.title("거북이로 그림그리기")
turtle.shape("turtle")
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick,1)
turtle.onscreenclick(screenMidClick,2)
turtle.onscreenclick(screenRightClick,3)

turtle.done()







