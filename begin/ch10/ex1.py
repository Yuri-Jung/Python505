#ex1

# tkinter : 윈도우 담당 모듈
from tkinter import *

window = Tk()
window.title('윈도우 창 연습')
window.geometry('400x100')
# window.resizable(width=FALSE, height=False) #FALSE와 False 둘 다 가능

label1 = Label(window, text='COOKBOOK~~ Python을 ')
label2 = Label(window, text='열심히',font=('궁서체',30), fg='blue')
label3 = Label(window, text='공부 중입니다.', bg='magenta', width=20, height=5, anchor=CENTER)

label1.pack()
label2.pack()
label3.pack()

window.mainloop()