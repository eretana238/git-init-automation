from tkinter import *
from selenium import webdriver
class Conn(Frame):
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
    url = 'https://www.github.com/login'
    browser = webdriver.Chrome()
    browser.get(url)
    login_user = browser.find_element_by_id('login_field')
    login_user.clear()
    login_user.send_keys(username)

if __name__ == '__main__':
    main = Tk()
    conn = Conn(main)
    main.mainloop()