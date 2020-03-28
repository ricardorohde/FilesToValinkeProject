from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from datetime import date
from unidecode import unidecode
import re

def colect_data(link):
    try:
        #Não esperar o carregamento completo
        caps = DesiredCapabilities().CHROME
        caps["pageLoadStrategy"] = "normal"  #  interactive

        # Dados para o selenium funcionar no windows
        options = Options()
        options.headless = False
        options.add_argument('--no-sandbox')  # Bypass OS security model
        options.add_argument('--disable-gpu')  # applicable to windows os only
        #options.add_argument('start-maximized')  #
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('window-size=1920x1480')

        driver = webdriver.Chrome(desired_capabilities=caps, options=options)

        dictDados = { "preco":"",
                      "link":"",
                      "nome":"",
                      "vendedor":"",
                      "linkimagem":"",
                      "loja":"",
                      "vendidos":"",
                      "estoqueAtual":"",
                      "estoqueInicial":"",
                      "erro":True
                      }



        driver.get(link)

        estoque = False
        
        try:
            if driver.find_element_by_xpath("//*[starts-with(@class, 'sale price')]").text != "":
                estoque = True
                print("Página existe")               
                    
        except Exception as e:
            print("Página com problemas", e)
        
        if estoque == True:
            print("Iniciando captura")
        
            vendedor = driver.find_element_by_class_name("seller").text
            preco = "R$" + driver.find_element_by_xpath("//*[starts-with(@class, 'sale price')]").text
            titulo = driver.find_element_by_class_name("produtoNome").text
            imagem = driver.find_element_by_class_name("photo").get_property("src")



            print("")
            print(titulo)
            print(vendedor)
            print(preco)
            print(link)
            print(imagem)
            print("")

            dictDados.update({"preco":preco,
                  "link":link,
                  "nome":titulo,
                  "vendedor":vendedor,
                  "linkimagem":imagem,
                  "loja":"Casas Bahia",
                  "vendidos":"",
                  "estoqueAtual":"",
                  "estoqueInicial":"",
                  "erro":False
                })
            
            print(dictDados)
            driver.quit()
            
    except:
        driver.quit()
        
        dictDados = { "preco":"",
                      "link":"",
                      "nome":"",
                      "vendedor":"",
                      "linkimagem":"",
                      "loja":"",
                      "vendidos":"",
                      "estoqueAtual":"",
                      "estoqueInicial":"",
                      "erro":True
                      }

    return dictDados
        










    
