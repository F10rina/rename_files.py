from tkinter import *
from tkinter import filedialog
#from os import *
#from os import path
import os


def st(file):
    return file.split('.')[-1]


def rename_files():
    i = 1
    #dir = filedialog.askdirectory()
    #name = dir.split('/')[-1]
    list_files = sorted(os.listdir(folder), key=st)
    print(name, list_files)
'''
    for file in list_files:
        ext = file.split('.')[-1]
        os.rename(f'{dir}/{file}', f'{dir}/{name}_{i}.{ext}')
        i = i + 1
'''

def choose_folder():
    dir = filedialog.askdirectory(initialdir='/')
    folder_name.insert(0, dir)
    global folder
    folder = folder_name.get()
    
def choose_name():
    global name
    name = file_name.get()


window = Tk()
window.geometry('400x250')
folder_lbl = Label(window, text="Folder:")
folder_lbl.grid(column=0, row=0)
folder_name = Entry(window, width=30, borderwidth=5)
folder_name.grid(column=1, row=0)
btn_dir = Button(window, text="Choose folder", command=choose_folder)
btn_dir.grid(column=2, row=0)

name_lbl = Label(window, text="New name:")
name_lbl.grid(column=0, row=1)
file_name = Entry(window,width=30, borderwidth=5)
file_name.grid(column=1, row=1)
btn_name = Button(window, text="Enter", command=choose_name)
btn_name.grid(column=2, row=1)

btn = Button(window, text="Переименовать", command=rename_files)
btn.grid(column=1, row=3)

window.mainloop()
