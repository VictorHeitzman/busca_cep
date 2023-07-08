from tkinter import *
from google_driver import Google

class Tela(Google):

    color_bg = '#282A36'
    font = 'arial 11'
    color_fg = 'white'
    color_bt = '#4F729A'

    def __init__(self):
        self.root = Tk()
        self.config()
        self.widgets()

        self.root.mainloop()

    def config(self):
        self.root.config(background=self.color_bg)
        self.root.title('Busca Cep')
        self.root.geometry('230x150+500+200')
        self.root.iconbitmap('img_route.ico')

    def widgets(self):

        self.txt_cep = Label(self.root,
                    text='Cep',
                    bg=self.color_bg,
                    fg=self.color_fg,
                    font=self.font).grid(row=0,column=0,sticky='W')

        self.txt_logradouro = Label(self.root,        
                    text=f'Logradouro: ',
                    font=self.font,
                    bg=self.color_bg,
                    fg=self.color_fg)
        self.txt_logradouro.grid(row=1,column=0,columnspan=2,sticky="W")

        self.txt_bairro = Label(self.root,
                    text=f'Bairro:',
                    font=self.font,
                    bg=self.color_bg,
                    fg=self.color_fg)
        self.txt_bairro.grid(row=2,column=0,columnspan=2,sticky="W")

        self.txt_uf = Label(self.root,
                    text=f'UF:',
                    font=self.font,
                    bg=self.color_bg,
                    fg=self.color_fg)
        self.txt_uf.grid(row=3,column=0,columnspan=2,sticky="W")

        self.txt_cep = Label(self.root,
                    text=f'CEP:',
                    font=self.font,
                    bg=self.color_bg,
                    fg=self.color_fg)
        self.txt_cep.grid(row=4,column=0,columnspan=2,sticky="W")

        self.button_pesquisar = Button(self.root,
                    text='pesquisar',
                    bg=self.color_bt,
                    fg=self.color_fg,
                    font=self.font,
                    width=10,
                    height=1,
                    command=self.search_cep)
        self.button_pesquisar.place(relheight=0.15,
                                    relwidth=0.35,
                                    relx=0.03,
                                    rely=0.80)

        self.button_abrir_maps = Button(self.root,
                    text='Abrir no maps',
                    bg=self.color_bt,
                    fg=self.color_fg,
                    font=self.font,
                    width=10,
                    height=1,
                    command=self.abrir_maps)
        self.button_abrir_maps.place(relheight=0.15,
                                     relwidth=0.50,
                                     relx=0.39,
                                     rely=0.80)

        self.input_pesquisa = Entry(self.root)
        self.input_pesquisa.place(relheight=0.12,relwidth=0.70,relx=0.18,rely=0.03)


        
        