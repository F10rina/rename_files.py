from tkinter import *
from tkinter import filedialog
from os import *
'''
# functions for rename
def file_extension(file):
    return file.split('.')[-1]
'''
def rename_folder():
    
    global name
    name = file_new.get()
    i = 1
    #folder_files = sorted(os.listdir(folder), key=file_extension)
    print(name, file_res)
'''
    for file in folder_files:
        ext = file.split('.')[-1]
        new_name = f'{name}_{i}.{ext}'
        if new_name in folder_files:
            i = i + 1
        else:
            os.rename(f'{folder}/{file}', f'{folder}/{name}_{i}.{ext}')
            i = i + 1
'''

# function for folder
def choose_folder():
    pass
'''
    dir = filedialog.askdirectory(initialdir='/')
    folder_name.insert(0, dir)
    global folder
    folder = folder_name.get()
'''
# function for files
def choose_files():
    
    global filenames
    filenames = filedialog.askopenfilenames(initialdir='/', title="Select files", filetypes=(('JPG files', '*.jpg'), ('all files', '*.*'), ('PDF files', '*.pdf')))
    # красота в окошке файлов.
    file_res = ', '.join([i.split('/')[-1] for i in filenames])
    files_lst.insert(0, file_res)

    
def rename_files():
    pass
    
window = Tk()
window.geometry('400x250')

# Choose folder
folder_lbl = Label(window, text="Folder:")
folder_lbl.grid(column=0, row=0)
folder_name = Entry(window, width=30, borderwidth=3)
folder_name.grid(column=1, row=0)
btn_dir = Button(window, text="Choose folder", command=choose_folder)
btn_dir.grid(column=2, row=0)

# Choose files
file_lbl = Label(window, text="Files:")
file_lbl.grid(column=0, row=1)
files_lst = Entry(window, width=30, borderwidth=3)
files_lst.grid(column=1, row=1)
btn_files = Button(window, text="Choose files", command=choose_files)
btn_files.grid(column=2, row=1)

# Enter new name
name_lbl = Label(window, text="New name:")
name_lbl.grid(column=0, row=2)
file_new = Entry(window,width=30, borderwidth=3)
file_new.grid(column=1, row=2)
file_new.insert(0, "fotochka")




btn = Button(window, text="Переименовать", command=rename_files)
btn.grid(column=1, row=3)

window.mainloop()
