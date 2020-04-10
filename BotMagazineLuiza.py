from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from datetime import date
import re
#import pandas as pd
from unidecode import unidecode
import json


def colect_data(link):
    try:
        #Não esperar o carregamento completo
        caps = DesiredCapabilities().CHROME
        caps["pageLoadStrategy"] = "eager"  #  interactive

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
        
        
        dictDados = {"preco":"",
                      "link":"",
                      "nome":"",
                      "vendedor":"",
                      "linkimagem":"",
                      "loja":"",
                      "vendidos":"",
                      "estoqueAtual":"",
                      "estoqueInicial":"",
                      "erro":""
                    }
        
        driver = webdriver.Chrome(desired_capabilities=caps, options=options) 
        driver.get(link)

        if "magazineluiza.com" in link:
            market_place = "Magazine Luiza"
        else:
            market_place = ""

        #Coleta dados do produto do link
        productInfo = driver.find_element_by_class_name('header-product').get_attribute('data-product')

        #Converte os dados para um dicionario
        dictProductInfo = json.loads(productInfo)

        #Tratando variável utilizada na url da imagem
        imageURL = dictProductInfo["imageUrl"].replace("{w}", "618")
        imageURL = imageURL.replace("{h}", "463")

        print("")
        print("Titulo: " + dictProductInfo["fullTitle"])
        print("Vendedor: " + dictProductInfo["seller"])
        print("Preço: R$" + dictProductInfo["listPrice"].replace(".",""))
        print("Loja: " + market_place)
        print("")

        dictDados.update({"preco":"R$" + dictProductInfo["bestPriceTemplate"].replace(".",""),
                          "link":link,
                          "nome":dictProductInfo["fullTitle"],
                          "vendedor":dictProductInfo["seller"],
                          "linkimagem":imageURL,
                          "loja":market_place,
                          "vendidos":"",
                          "estoqueAtual":"",
                          "estoqueInicial":"",
                          "erro":False
                        })

        if dictDados["nome"] == "" and dictDados["vendedor"] == "":
            dectDados["link"] = link
            dictDados["erro"] = True

        driver.quit()
    except:
        try:
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
        except:
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

