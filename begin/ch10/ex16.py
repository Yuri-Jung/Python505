from tkinter import *
from tkinter.filedialog import *

window = Tk()
window.geometry('400x100')

label1 = Label(window, text='선택한 이미지 파일 : ')
label1.pack()

saveFp = asksaveasfile(parent=window, mode='w', defaultextension='.jpg',
                       filetypes=(('jpg파일','.jpg;*.jpeg'),('모든파일','*.*')))
# mode='w' = write 모드이다
label1.configure(text=saveFp)
saveFp.close()

window.mainloop()