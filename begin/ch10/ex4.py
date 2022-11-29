from tkinter import *
from tkinter import messagebox

def myFunc():
    messagebox.showinfo('강아지 버튼','강아지가 귀엽죠? ^^ 제 강아지입니다')
window = Tk()
photo = PhotoImage(file='gif/dog2.gif')
button1 = Button(window, image=photo, command=myFunc)
# 사진 클릭하면 창이 뜬다

button1.pack()

window,mainloop()