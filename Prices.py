import requests as rq
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import os

date =[]
datainicial = datetime(2025, 1, 7).date()
datafinal = datetime.now().date() #dia atual
values = []
timestamps = []
tempoMinuto = []

while datafinal >= datainicial:
    date.append(datafinal)
    datafinal -= timedelta(days=1)

for e in date:
    url = f"https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=1&date={e}"
    dados_json = rq.get(url, timeout=30)
    dados = dados_json.json()
    valores = dados['prices']
    values.append([valor[1] for valor in valores ])
    timestamps.append([tamp[0] for tamp in valores])

for ts in timestamps[0]:
    #Converter para datetime
    dt = datetime.fromtimestamp(ts / 1000)  # Dividindo por 1000 para converter ms para s
    minutos = dt.strftime("%Y-%m-%d %H:%M")  # Formatar como HH:MM (hora:minuto)
    tempoMinuto.append(minutos)

#gerando e salvando a imagem

image_path = 'btc/grafico.png'
fig, sub = plt.subplots()
sub.plot(tempoMinuto, values[0])
plt.xticks([tempoMinuto[0], tempoMinuto[-1]])

fig.savefig(image_path)

plt.close(fig)


