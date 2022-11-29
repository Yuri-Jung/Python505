from tkinter import *
from tkinter import messagebox
window = Tk()

def func_open():
    messagebox.showinfo('메뉴 선택','열기 메뉴를 선택함')

def func_exit():
    window.quit()
    window.destroy()

mainMenu = Menu(window)
window.configure(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label='파일', menu=fileMenu)
fileMenu.add_command(label='열기', command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label='종료', command=func_exit)

window.mainloop()