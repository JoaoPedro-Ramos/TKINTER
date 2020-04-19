"PÁGINA DE LOGIN DO USUÁRIO"

from tkinter import *


class Login:

    def __init__(self, login):
        Label(login, text='FUNCIONA', width=10).pack()




def init_login(cont):
    if cont == True:
        root = Tk()
        root.geometry('270x570')
        Login(root)    
        root.mainloop()


