from tkinter import *
from tkinter import messagebox

window = Tk()

def myFunc():
    if chk.get() ==0:
        messagebox.showinfo('', '체크버튼이 꺼졌습니다')
    else:
        messagebox.showinfo('','체크버튼이 켜졌습니다')
chk = IntVar() #정수 변수 선언
# 전역변수
cb1 = Checkbutton(window,text='클릭하세요', variable=chk, command=myFunc)

cb1.pack()

window.mainloop()