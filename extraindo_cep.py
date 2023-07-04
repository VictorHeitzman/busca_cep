from selenium import webdriver as driver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd
from tkinter import *

from selenium.webdriver.common.by import By

#VAR
color_bg = '#282A36'
font = 'arial 11'
color_fg = 'white'
color_bt = '#4F729A'
endereco = []


root = Tk()
root.config(background=color_bg)
root.title('Buscar Cep')
root.geometry('300x300+500+200')



    

def cep_is_valid(cep):
    
    if cep.isdigit():

        if len(cep) <= 8:
            print('Coletando dados... aguarde! ')
            
            browser.find_element(By.NAME, 'endereco').send_keys(cep)

            sleep(3)

            #Clicando em pesquisar
            browser.find_element(By.NAME, 'btn_pesquisar').click()

            sleep(3)
            return cep
        else:
            print('digite apenas os 8 números de um cep')
            search_cep()
            
    else: 
        print('tente escrever apenas números:')  
        search_cep()
    
def create_dataFrame(dados):

    for p, dado in enumerate(dados):
        endereco.append(dado.text)

    end_ = [endereco.copy()]
    #criando dataframe com os dados
    df = pd.DataFrame(end_, columns=['logradouro','bairro','UF','cep'])  
    
    df.to_csv('correios.csv', index=None, encoding='utf-8')
    
    print(df)

    return print('df salvo!')
    
def search_cep():
    cep = str(input('digite o cep: '))
    cep_is_valid(cep)

label = Label(root,
              text='Cep',
              bg=color_bg,
              fg=color_fg,
              font=font).grid(row=0,column=0)

button_pesquisar = Button(root,
                          text='pesquisar',
                          bg=color_bt,
                          fg=color_fg,
                          font=font).grid(row=0,column=2)

input_pesquia = Entry(root).grid(row=0,column=1)

options = driver.ChromeOptions()
options.add_argument('--headless=new')

browser = driver.Chrome(options=options)
browser.get('https://buscacepinter.correios.com.br/app/endereco/index.php')

search_cep()

#Buscando quantidade de colunas na página
dados =  browser.find_elements(By.XPATH,'//td')

create_dataFrame(dados)


browser.quiT()
root.mainloop()


