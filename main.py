from tkinter import *
from tkinter import filedialog
import os
import subprocess
import conn
import time


class Main(Frame):
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

        create_project_folder = Button(frame, text='Create', width=20, height=1,
                                       command=lambda: create_project(self.master, project_name.get()))
        create_project_folder.pack(side=RIGHT)


def choose_folder():
    folder = filedialog.askdirectory(parent=main,
                                     initialdir=os.getcwd(),
                                     title="Select projects folder:")
    with open('create_folder.bat', 'r') as file:
        # read list of lines
        data = file.readlines()
    # add directory
    data[0] = 'cd ' + folder + '\n'

    with open('create_folder.bat', 'w') as file:
        file.writelines(data)


def create_project(frame, project_name):
    with open('create_folder.bat', 'r') as file:
        # read list of lines
        data = file.readlines()
    # create directory
    data[1] = 'mkdir ' + project_name + '\n'
    data[2] = 'cd ' + project_name + '\n'

    with open('create_folder.bat', 'w') as file:
        file.writelines(data)
    # init project creation
    subprocess.call([r'create_folder.bat'])
    frame.destroy()
    git = conn.browse('eretana238', 'ImAKnight61', project_name)

    with open('update_origin.bat', 'r') as file:
        data = file.readlines()
    data[0] = 'cd ' + project_name + '\n'
    data[1] = 'git remote add origin {}\n'.format(git)
    with open('update_origin.bat', 'w') as file:
        file.writelines(data)
    subprocess.call([r'update_origin.bat'])

if __name__ == '__main__':
    main = Tk()
    open_folder = Main(main)
    main.mainloop()


