from tkinter import *
import register as RG
import log_in


class TelaInicial:

    def __init__(self, master):
        self.master = master
        self.container1 = Frame(master)
        self.container2 = Frame(master)
        self.container3 = Frame(master)
        self.container4 = Frame(master)
        self.container1.pack()
        self.container2.pack(pady=30)
        self.container3.pack()
        self.container4.pack(pady=10)
    
    def screen(self):
        self.texto = Label(self.container2, font=('Arial', '12', 'bold'), text='WELCOME!')
        self.texto.pack()

        Label(self.container3, 
        text='Hello \nif you already account here\n please, click in log in... \nElse\n please create your account\n click in register.',
        font=('Arial', '10', 'normal'), width=140).pack()
        Button(self.container4, text='register', command=lambda: [self.quit(), self.register_()]).pack(side=LEFT)
        Button(self.container4, text='Log in', command=lambda: [self.quit(), self.login()]).pack(side=LEFT)
        

    def quit(self):
        self.master.destroy()

    def register_ (self):
        RG.raiz = Tk()
        RG.raiz.geometry('270x570')
        RG.Inicial(RG.raiz).tela()
        RG.raiz.mainloop()

    def login(self):
        log_in.init_login(True)

def apresentation_screen():
    cont = 1
    if cont == 1:
        root = Tk()
        root.geometry('270x570')
        TelaInicial(root).screen()
        root.mainloop()
        cont += 1


apresentation_screen()