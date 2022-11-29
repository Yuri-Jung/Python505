#ex2.py

from tkinter import *
window = Tk()

photo = PhotoImage(file='gif/dog.gif')
# photo = PhotoImage(file='ㅎ/dog.gif')
# 대소문자 구별 안한다
label1 = Label(window, image=photo)

label1.pack()

window.mainloop()
# 대문자로 시작하는 건 클래스라고 생각하면 좋음