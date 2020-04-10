# coding: utf-8

# IMPORTA BIBLIOTECAS E APIS
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from unidecode import unidecode
from datetime import date
#import pandas as pd
import re
import time

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

        driver = webdriver.Chrome(desired_capabilities=caps, options=options)

        #dfLinks = pd.DataFrame([link])
        #dfLinks

        listaDados = []
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


        if "submarino.com" in link:
            market_place = "Submarino"
        else:
            market_place = ""



        #for index, row in dfLinks.iterrows():
        if 1 == 1:
            driver.get(link)
            
            #Vê se é o captcha
            try:
                captcha = driver.find_element_by_class_name('page-title').text
                if captcha == "Please verify you are a human":
                    print("CAPTCHA DE VERIFICAÇÃO")
                    input('Resolva o captcha e tecle enter:')
            except:
                pass
            
               #Vê se é layout antigo
            try:
                driver.find_element_by_xpath("//*[starts-with(@class, 'seller-')]").text
                layout = "antigo"
            except Exception as e:
                layout = "naoantigo"
                #print(e)
                print("Erro ao buscar no layout antigo")
                pass
            
            #Vê se é layout novo
            try:
                driver.find_element_by_xpath('//*[@id="content"]/div/div/div[2]/div/section/div/div[2]/div[2]/div/div[3]/div[2]/span/a').text
                layout = "novo"
            except Exception as e:
                #layout = "naonovo"
                #print(e)
                print("Erro ao buscar no layout novo")
                pass
            
            #Vê se tem estoque
            try:
                estoque = driver.find_element_by_id('title-stock').text
            except Exception as e: 
                #print(e)
                print("Sem estoque")
                estoque = ""
                pass
            
            print(estoque)
            print("O layout dessa página é: ", layout)
            
            
            #Se o layout for antigo, busca pelos dados antigos.
            if estoque != "Ops! Já vendemos o estoque" and layout == "antigo":

                vendedor = driver.find_element_by_xpath("//*[starts-with(@class, 'seller-')]").text
                vendedor = vendedor.replace("\n", " ")
                preco = driver.find_element_by_class_name("sales-price").text
                titulo = driver.find_element_by_id("product-name-default").text
                imagem = driver.find_element_by_class_name('image-gallery-image')
                imagem = imagem.find_element_by_tag_name('img').get_attribute('src')

                
                print(titulo)
                print(vendedor)
                print(preco)
                print(imagem)
                print("")
                
                dictDados.update({"preco":preco.replace(".",""),
                      "link":link,
                      "nome":titulo,
                      "vendedor":vendedor,
                      "linkimagem":imagem,
                      "loja":market_place,
                      "vendidos":"",
                      "estoqueAtual":"",
                      "estoqueInicial":"",
                      "erro":False
                    })
                listaDados.append(dictDados.copy())
            
            
            #Se o layout for novo, busca pelos dados do layout novo
            elif estoque != "Ops! Já vendemos o estoque" and layout == "novo":

                vendedor = driver.find_element_by_xpath('//*[@id="content"]/div/div/div[2]/div/section/div/div[2]/div[2]/div/div[3]/div[2]/span/a').text
                vendedor = vendedor.replace("\n", " ")
                preco = driver.find_element_by_xpath('//*[@id="content"]/div/div/div[2]/div/section/div/div[2]/div[2]/div/div[1]/div[1]/div/div/span').text
                titulo = driver.find_element_by_id("product-name-default").text
                imagem = driver.find_element_by_class_name('image-gallery-image')
                imagem = imagem.find_element_by_tag_name('img').get_attribute('src')

                print(titulo)
                print(vendedor)
                print(preco)
                print(imagem)
                print("")
                
                dictDados.update({"preco":preco.replace(".",""),
                      "link":link,
                      "nome":titulo,
                      "vendedor":vendedor,
                      "linkimagem":imagem,
                      "loja":market_place,
                      "vendidos":"",
                      "estoqueAtual":"",
                      "estoqueInicial":"",
                      "erro":False
                    })
                listaDados.append(dictDados.copy())

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
