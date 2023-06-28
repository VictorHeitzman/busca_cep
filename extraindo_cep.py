from selenium import webdriver as driver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd

from selenium.webdriver.common.by import By

endereco = []

def cep_is_valid(cep) -> str:
    
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
    
def search_cep() -> str:
    cep = str(input('digite o cep: '))
    cep_is_valid(cep)

options = driver.ChromeOptions()
options.add_argument('--headless=new')

browser = driver.Chrome(options=options)
browser.get('https://buscacepinter.correios.com.br/app/endereco/index.php')

search_cep()

#Buscando quantidade de colunas na página
dados =  browser.find_elements(By.XPATH,'//td')

create_dataFrame(dados)

print('Finalizado!')

browser.quit()

