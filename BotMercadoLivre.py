# coding: utf-8

# IMPORTA BIBLIOTECAS E APIS
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from datetime import date

import time
import re
#import pandas as pd
import time
import requests
import json

def colect_data(link):
    # Dados para o selenium funcionar no windows
    options = Options()
    options.headless = True
    options.add_argument('--no-sandbox')  # Bypass OS security model
    options.add_argument('--disable-gpu')  # applicable to windows os only
    #options.add_argument('start-maximized')  #
    options.add_argument('disable-infobars')
    options.add_argument("--disable-extensions")
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('window-size=1920x1480')

    driver = webdriver.Chrome(options=options)





    driver.get('https://mercadolivre.com.br')
        
    listaDados = []
    dictDados = { "preco":"",
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

    if "mercadolivre.com" in link:
        market_place = "Mercado Livre"
    else:
        market_place = ""

    #Tratamendo do ID do link
    inicio_id = link.find("MLB-")
    final_id = link.find("-", inicio_id+4)
    id_produto = link[inicio_id:final_id].replace("-","")
        
    #print("O LINK: ")
    #print('https://api.mercadolibre.com/items/'+ i.get_attribute('value'))
    #jsonItem = requests.get('https://api.mercadolibre.com/items/'+ i.get_attribute('value'))
    jsonItem = requests.get('https://api.mercadolibre.com/items/' + id_produto)
    jsonItem = json.loads(jsonItem.text)
    #print(i.get_attribute('value'))
    print("marca: ", jsonItem['attributes'][0]['value_name'])
    preco = jsonItem['base_price']
    data_criacao = jsonItem['date_created']
    link = jsonItem['permalink']
    imagem = jsonItem['pictures'][0]['url']
    titulo = jsonItem['title']
                
                              
    id_vendedor = jsonItem['seller_id']
    vendedor = requests.get("https://api.mercadolibre.com/users/" + str(id_vendedor))
    vendedor = json.loads(vendedor.text)
    vendedor = vendedor['nickname']
    estoqueinicial = jsonItem['initial_quantity']
    vendidos = jsonItem['sold_quantity']
    estoqueAtual = estoqueinicial - vendidos
                

                
    print("")
    print("Preço: R$", "%.2f" % preco)
    print("Link: " + link)
    print("Titulo: " + titulo)
    print("Vendedor: " + vendedor)
    print("DataCadastro: " + data_criacao)
    print("UrlImagem: " + imagem)
    print("Estoqueinicial: " + str(estoqueinicial))
    print("Vendidos: " + str(vendidos))
    print("EstoqueAtual: " + str(estoqueAtual))
                
                
    print("")
    dictDados.update({"preco":"R$ "+str("%.2f" % preco).replace(".",","),
                        "link":link,
                        "nome":titulo,
                        "vendedor":vendedor,
                        "linkimagem":imagem,
                        "loja":"Mercado Livre",
                        "vendidos":str(vendidos),
                        "estoqueAtual":str(estoqueAtual),
                        "estoqueInicial":str(estoqueinicial),
                        "erro":False
                    })
    listaDados.append(dictDados.copy())

    if dictDados["nome"] == "" and dictDados["vendedor"] == "":
        dictDados["link"] = link
        dictDados["erro"] = True

    driver.quit()
    
    return dictDados

