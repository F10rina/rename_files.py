
from tkinter import *
import os
from os import path
from tkinter import filedialog

def st(file):
    return file.split('.')[-1]


def rename_files():
    i = 1
    dir = 'E:/foto'
    name = 'name_foto'
    list_files = sorted(os.listdir(dir), key=st)
#    print(list_files)
    for file in list_files:
        ext = file.split('.')[-1]
        os.rename(f'{dir}/{file}', f'{dir}/{name}_{i}.{ext}')

#        print(os.listdir(dir))
        i = i + 1



window = Tk()
window.geometry('400x250')
lbl = Label(window, text="Путь")
lbl.grid(column=0, row=0)
txt = Entry(window,width=10)
txt.grid(column=1, row=0)

lbl1 = Label(window, text="Название")
lbl1.grid(column=0, row=1)
txt1 = Entry(window,width=10)
txt1.grid(column=1, row=1)

btn = Button(window, text="Переименовать", command=rename_files)
btn.grid(column=0, row=3)

dir = filedialog.askdirectory()
print(dir)

window.mainloop()


