from tkinter import *
import log_in

class Inicial:

    def __init__(self, inicio):
        self.inicio = inicio
        self.frame1 = Frame(inicio)
        self.frame1.pack()
        self.frame2 = Frame(inicio, pady=10)
        self.frame2.pack()
        self.frame3 = Frame(inicio)
        self.frame3.pack()
        self.frame4 = Frame(inicio, pady=15)
        self.frame4.pack()

    def tela(self):
        self.texto01 = Label(self.frame1, text='REGISTER', fg='black', font=('Verdana', '10', 'bold'), height=3, width=20)
        self.texto01.pack()
        Label(self.frame2, text='Name:', fg='black', width=8, font=('verdana', '10', 'bold')).pack(side=LEFT)

        self.name = Entry(self.frame2, width=10, font=('Verdana', '10', 'bold'))
        self.name.focus_force()
        self.name.pack(side=LEFT)

        Label(self.frame3, text='Password:', fg='black', font=('Verdana', '10', 'bold'), width=8).pack(side=LEFT)
        self.password = Entry(self.frame3, width=10, show='*', font=('Verdana', '10', 'bold'))
        self.password.pack(side=LEFT)

        Button(self.frame4, text='Register', font=('Verdana', '10', 'bold'), bg='pink', command=self.pega_dados).pack()
        self.menssage = Label(self.frame4, font=('Verdana', '10', 'bold'), height=3, text='Waiting...', fg='black')
        self.menssage.pack()

    def pega_dados(self):
        NAME =self.name.get()
        PASSWORD = self.password.get()
        self.conferir(NAME, PASSWORD)
    
    def conferir(self, a, b):
        if a == '' or b == '':
            self.menssage ['text'] = 'MISSING DATA'
            self.menssage ['fg'] = 'red'

        elif a == b:
            self.menssage ['text'] = 'AUTHORIZED ACCESS'
            self.menssage ['fg'] = 'green'
            self.inicio.destroy()
            log_in.init_login(True)

        else:
            self.menssage ['text'] = 'ACCESS DENIED'
            self.menssage ['fg'] = 'red'


