import json
import sys
import BotShoptime as shoptime
import BotAmericanas as americanas
import BotSubmarino as submarino
import BotMercadoLivre as ML
import BotMagazineLuiza as magazineluiza

# Recebe parametro na variável "link"
link = sys.argv[1]
link = link.replace("{#}", "&")
link = link.replace("{-}", "?")

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
else:
    print("A URL informada não faz parte da lista de sites validos")


gerarArquivo = open("DadosProduto.txt", 'w')
gerarArquivo.write(json.dumps(data))
gerarArquivo.close()


print("{")
for dict_key, dict_value in data.items():
    print("\t\"" + dict_key + "\": \"" + str(dict_value) + "\",")
print("}")
