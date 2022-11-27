import os
from tkinter import *
from tkinter import filedialog


def rename_all():

    new_name = filename_new.get()
    i = 1
    #print(new_name, rb.get(), folder, files_array)
    #print(new_name, rb.get(),folder, folder_files)

    for file in files_array:
        ext = file.split('.')[-1]
        r_name = f'{new_name}_{i}.{ext}'
        while True:
            if r_name in os.listdir(folder):
                i = i + 1
                r_name = f'{new_name}_{i}.{ext}'
            else:
                os.rename(f'{folder}/{file}', f'{folder}/{r_name}')
                i = i + 1
                break


# function for choosing folder
def choose_folder():

    global folder
    global files_array
    dir = filedialog.askdirectory(initialdir='/')
    folder_name.insert(0, dir)
    folder = folder_name.get()
    files_array = os.listdir(folder)


# function for choosing files
def choose_files():

    global folder
    global files_array
    filenames = filedialog.askopenfilenames(initialdir='/', title="Select files", filetypes=(('JPG files', '*.jpg'), ('all files', '*.*'), ('PDF files', '*.pdf')))
    folder = '/'.join(filenames[0].split('/')[:-1])
    # красота в окошке файлов.
    files_res = ', '.join([i.split('/')[-1] for i in filenames])
    files_lst.insert(0, files_res)
    files_array = files_res.split(', ')


def button_state(value):
    if value == 'folder':
        btn_dir['state'] = NORMAL
        btn_files['state'] = DISABLED
    if value == 'files':
        btn_dir['state'] = DISABLED
        btn_files['state'] = NORMAL



window = Tk()
window.geometry('400x250')

# Choose folder
#folder_lbl = Label(window, text="Folder:")
#folder_lbl.grid(column=0, row=0)
var = StringVar()
var.set('folder')
radio_folder = Radiobutton(window, text='Folder', variable=var, value='folder', command=lambda: button_state(var.get()))
radio_folder.grid(column=0, row=0, sticky=W)

folder_name = Entry(window, width=30, borderwidth=3)
folder_name.grid(column=1, row=0)
btn_dir = Button(window, text="Choose folder", padx=15, command=choose_folder)
btn_dir.grid(column=2, row=0, sticky=W)

# Choose files
#file_lbl = Label(window, text="Files:")
#file_lbl.grid(column=0, row=1)
radio_files = Radiobutton(window, text='Files:', variable=var, value='files', command=lambda: button_state(var.get()))
radio_files.grid(column=0, row=1, sticky=W)

files_lst = Entry(window, width=30, borderwidth=3)
files_lst.grid(column=1, row=1)
btn_files = Button(window, text="Choose files", padx=20, state=DISABLED, command=choose_files)
btn_files.grid(column=2, row=1, sticky=W)

# Enter new name
newname_lbl = Label(window, text="New name:")
newname_lbl.grid(column=0, row=2)
filename_new = Entry(window,width=30, borderwidth=3)
filename_new.grid(column=1, row=2)
filename_new.insert(0, "fotochka")

# Rename button
btn = Button(window, text="Переименовать", command=rename_all)
btn.grid(column=1, row=3)

window.mainloop()