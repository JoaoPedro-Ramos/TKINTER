"PÁGINA DE LOGIN DO USUÁRIO"

from tkinter import *


class Login:

    def __init__(self, login):
        self.login = login
        self.container = Frame(login)
        self.container1 = Frame(login)
        self.container2 = Frame(login)
        self.container3 = Frame(login)
        self.container4 = Frame(login)
        self.container.pack()
        self.container1.pack(pady=20)
        self.container2.pack()
        self.container3.pack(pady=20)
        self.container4.pack()
        self.screen()

    def screen(self):
        self.text = Label(self.container1, text='LOG IN', fg='black', font=('Verdana', '10', 'bold'), height=3, width=20)
        self.text.pack()
        Label(self.container2, text="Hello\n I'm glad you're here!\n Continue your journey by filling\n out the form below.").pack()
        Label(self.container3, text='Username:').pack(side=LEFT)
        self.username = Entry(self.container3, width=20)
        self.username.pack(side=LEFT)
        Label(self.container4, text='Password:').pack(side=LEFT)
        self.password = Entry(self.container4, width=20, show='*')
        self.password.pack(side=LEFT)
        




def init_login(cont):
    if cont == True:
        root = Tk()
        root.geometry('270x570')
        Login(root)    
        root.mainloop()
