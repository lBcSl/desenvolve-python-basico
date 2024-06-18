#QUESTAO 03

import datetime

data_live = datetime.datetime.now()

print (f"Data de hoje e: {data_live}")

data_live_formatada = data_live.strftime("%d/%m/%Y %H:%M:%S")
print (f"Data de Hoje formatada: {data_live_formatada}")