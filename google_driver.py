from selenium import webdriver as driver
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd

class Google:

    
    def __init__(self):
        pass
       
    def abrir_google(self):
        self.options = driver.ChromeOptions()
        self.options.add_argument('--headless=new')
        self.browser = driver.Chrome(options=self.options)
        self.browser.get('https://buscacepinter.correios.com.br/app/endereco/index.php')
     
    def salvar_df(self):
        self.df.to_csv('correios.csv', index=None, encoding='utf-8')
    
    def search_cep(self):
        self.cep = self.input_pesquisa.get()
        self.abrir_google()
        self.browser.find_element(By.NAME, 'endereco').send_keys(self.cep)

        sleep(1)

        #Clicando em pesquisar
        self.browser.find_element(By.NAME, 'btn_pesquisar').click()

        sleep(1)

        self.dados = self.browser.find_elements(By.XPATH,'//td')
        
        self.create_dataframe()

    
    def create_dataframe(self):
        
        self.endereco = []
        for p, dado in enumerate(self.dados):
            self.endereco.append(dado.text)
            print(dado.text)
        
        self.txt_logradouro.config(text=f'Logradouro: {self.endereco[0]}')
        self.txt_bairro.config(text=f'Bairro: {self.endereco[1]}')
        self.txt_uf.config(text=f'UF: {self.endereco[2]}')
        self.txt_cep.config(text=f'CEP: {self.endereco[3]}')


        self.end_ = [self.endereco.copy()]
        #criando dataframe com os dados
        self.df = pd.DataFrame(self.end_, columns=['logradouro','bairro','UF','cep'])  

    def abrir_maps(self):
        self.cep = self.input_pesquisa.get()
        self.options = driver.ChromeOptions()
        #self.options.add_argument('--headless=new')
        self.browser = driver.Chrome()
        self.browser.get(f'https://www.google.com.br/maps/@-23.4904756,-46.3504787,17z?entry=ttu')

        self.browser.find_element(By.XPATH,'//*[@id="searchboxinput"]').send_keys(self.cep)
        self.browser.find_element(By.XPATH, '//*[@id="hArJGc"]').click()
        sleep(2)
        self.browser.find_element(By.XPATH,'//*[@id="omnibox-directions"]/div/div[4]').click()