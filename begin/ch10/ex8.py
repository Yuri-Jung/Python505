#ch10 ex.8

from tkinter import *

window = Tk()
window.geometry("200x200")

butList = ['']*3

for i in range(0,3):
    butList[i] = Button(window, text='버튼' + str(i+1))

for btn in butList:
    # btn.pack(side = RIGHT)
    # btn.pack(side =TOP)
    # btn.pack(side = BOTTOM)
    # btn.pack(side = TOP, fill=X)
    # btn.pack(side=TOP, fill=X, padx=10, pady=10)
    btn.pack(side=TOP, fill=X, ipadx=10, ipady=10, padx=10, pady=10) # 여백 넣어주기

window.mainloop()



