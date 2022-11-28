from myTurtle import *
import turtle

# 전역변수
inStr = ''
swidth, sheight =300,300
tx, ty, tAngle, txtSize = [0]*4


turtle.title('거북 글자 쓰기(모듈버전)')
turtle.shape('turtle')
turtle.setup(width=swidth+50, height=sheight+50)
turtle.screensize(swidth,sheight)
turtle.penup()
turtle.speed(5)

inStr = getString()
for ch in inStr:
    tx,ty,tAngle,txtSize = getXYAS(swidth,sheight)
    r,g,b = getRGB()

    turtle.goto(tx,ty)
    turtle.left(tAngle)
    turtle.pencolor((r,g,b))
    turtle.write(ch,font=('맑은고딕', txtSize, 'bold'))

turtle.done()








