from flask import Flask
import json
import BotShoptime as shoptime
import BotAmericanas as americanas
import BotSubmarino as submarino
import BotMercadoLivre as ML
import BotMagazineLuiza as magazineluiza
import BotCasasBahia as casasbahia

app = Flask(__name__)

@app.route("/<link>")
def GetLink(link):

    link = link.replace("{+}", "/")
    
    if "americanas.com" in link:
        data = americanas.colect_data(link)
    elif "shoptime.com" in link:
        data = shoptime.colect_data(link)
    elif "submarino.com" in link:
        data = submarino.colect_data(link)
    elif "magazineluiza.com" in link:
        data = magazineluiza.colect_data(link)
    elif "mercadolivre.com" in link:
        data = ML.colect_data(link)
    elif "casasbahia.com" in link:
        data = casasbahia.colect_data(link)
    else:
        data = { "preco":"",
                  "link":link,
                  "nome":"",
                  "vendedor":"",
                  "linkimagem":"",
                  "loja":"",
                  "vendidos":"",
                  "estoqueAtual":"",
                  "estoqueInicial":"",
                  "erro":True
                  }

    json_data = json.dumps(data)
    print(json_data)
    
    return json_data

if __name__ == "__main__":
    app.run(port=5060)
