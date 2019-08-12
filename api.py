from tkinter import *
import requests

class Api(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.title('Github credentials')
        self.master.geometry('200x150')

        frame = Frame(self.master)
        frame.pack()

        label_username = Label(frame, text='Username')
        label_username.pack()

        username = Entry(frame)
        username.pack()

        label_password = Label(frame, text='Password')
        label_password.pack()

        password = Entry(frame)
        password.pack()

        submit = Button(frame, text='SUBMIT', command=lambda: api_conn(username.get(), password.get()))
        submit.pack()

def api_conn(username, password):
    # get_api = requests.get('https://api.github.com/user', auth=(username, password))
    post_api = requests.post('https://api.github.com/user/repos', auth=(username, password))
    # print(get_api.json())
    print(post_api.json())

if __name__ == '__main__':
    main = Tk()
    conn = Api(main)
    main.mainloop()