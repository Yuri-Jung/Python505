'''
title : 거북이 나선모양 글자쓰기

'''

import turtle
import random
import math
from tkinter.simpledialog import *

# 전역변수
inStr = ''
swidth, sheight = 500,500
tx, ty, txtSize = [0]*3



turtle.title('거북 글자 쓰기')
turtle.shape('turtle')
turtle.setup(width=swidth+50, height=sheight+50)
turtle.screensize(swidth,sheight)
turtle.penup()

inStr = askstring('문자열입력', '거북이 쓸 문자열을 입력')
dist = 200
angle = 0
value = int(360*2 / len(inStr))

for ch in inStr:
    rad = 3.141592 * angle / 180
    tx = dist * math.cos(rad)
    ty = dist * math.sin(rad)
    dist -= 200 / len(inStr)
    angle += value
    r = random.random()
    g = random.random()
    b = random.random()
    txtSize = random.randrange(10,20)
    # txtSize = random.randrange(10,50)



    turtle.goto(tx,ty)
    turtle.pencolor((r,g,b))
    turtle.write(ch, font=('맑은고딕', 20, 'bold'))

turtle.done()