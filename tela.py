from tkinter import *
class Tela():

    color_bg = '#282A36'
    font = 'arial 11'
    color_fg = 'white'
    color_bt = '#4F729A'
    
    def __init__(self) -> None:
        self.root = Tk()
        self.config()
        self.labels()
        #self.butons()
        self.inputs()

        self.root.mainloop()

    def config(self):
        self.root.config(background=self.color_bg)
        self.root.title('Buscar Cep')
        self.root.geometry('300x300+500+200')
    
    def labels(self):
        self.label = Label(self.root,
                           text='Cep',
                           bg=self.color_bg,
                           fg=self.color_fg,
                           font=self.font).grid(row=0,column=0)


    def butons(self):
        self.button_pesquisar = Button(self.root,
                                       text='pesquisar',
                                       bg=self.color_bt,
                                       fg=self.color_fg,
                                       font=self.font).grid(row=0,column=2)

    def inputs(self):
        self.input_pesquia = Entry(self.root).grid(row=0,column=1)

        driver = Driver()
        

        
