"PÁGINA DE AGRADECIMENTO AO USUÁRIO POR TER FEITO O REGISTRO"

from tkinter import *
import log_in as lg

class Thanks:

    def __init__(self, Thanks):
        self.Thanks = Thanks
        self.container = Frame(Thanks)
        self.container1 = Frame(Thanks)
        self.container2 = Frame(Thanks)
        self.container.pack(pady=30)
        self.container1.pack(pady=40)
        self.container2.pack(pady=50)
        self.screen()

    def screen(self):
        self.text = Label(self.container, text='THANK YOU!', fg='black', font=('Verdana', '10', 'bold'), height=3, width=20)
        self.text.pack()
        Label(self.container1, text="THANKS").pack()
        Label(self.container2, text='click here to be redirected').pack()
        Button(self.container2, bg='purple', width=10, command=self.login).pack()
        
    def login(self):
        self.Thanks.destroy()
        lg.init_login(True)

def init_thanks(ini):
    if ini == True:
        root = Tk()
        root.geometry('270x570')
        Thanks(root)    
        root.mainloop()
