from tkinter import *
from tkinter import filedialog
import os
import subprocess

class api(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.title('Automation')
        self.master.resizable(width=False, height=False)
        self.master.geometry('400x200')

        frame = Frame(self.master)
        frame.pack()

        label_folder = Label(frame, text='Choose where to create your project')
        label_folder.pack(side=TOP)

        select_folder = Button(frame, text='Choose Folder', width=20, height=2, command=lambda: choose_folder())
        select_folder.pack()

        project_name = Entry(frame, width=20, bd=1)
        project_name.pack(side=LEFT)

        create_project_folder = Button(frame, text='Create', width=20, height=1, command=lambda: create_project(project_name.get()))
        create_project_folder.pack(side=RIGHT)

def choose_folder():
    folder = filedialog.askdirectory(parent=main,
                                     initialdir=os.getcwd(),
                                     title="Select projects folder:")
    with open('init.bat', 'r') as file:
        # read list of lines
        data = file.readlines()
    # add directory
    data[0] = 'cd '+folder + '\n'
    print(data)

    with open('init.bat', 'w') as file:
        file.writelines(data)

def create_project(project_name):
    with open('init.bat', 'r') as file:
        # read list of lines
        data = file.readlines()
    # create directory
    data[1] = 'mkdir ' + project_name + '\n'
    data[2] = 'cd ' + project_name + '\n'

    with open('init.bat', 'w') as file:
        file.writelines(data)
    # init project creation
    subprocess.call([r'init.bat'])


main = Tk()
open_folder = api(main)
main.mainloop()
