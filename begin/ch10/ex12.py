#ch10 ex12

from tkinter import *
from tkinter import messagebox

def clickImage(event):
    messagebox.showinfo('마우스','토끼에서 마우스 클릭됨')

window = Tk()
window.geometry('400x400')

photo = PhotoImage(file='gif/rabbit.gif')
label1 = Label(window, image=photo)
label1.bind('<Button>', clickImage)
# 3개의 버튼 다 클릭하면

label1.pack(expand=True, anchor=CENTER)

window.mainloop()