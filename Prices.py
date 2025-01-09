import requests as rq
import pandas as pd 
import matplotlib.pyplot as pl

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana,dogecoin&vs_currencies=usd,brl"
dados_json = rq.get(url, timeout=3)

dados = dados_json.json()

#BITCOIN
btcDolar = dados['bitcoin']['usd']
btcReal = dados['bitcoin']['brl']

#ETHEREUM
ethDolar = dados['ethereum']['usd']
ethReal = dados['ethereum']['brl']

#SOLANA
solDolar = dados['solana']['usd']
solReal = dados['solana']['brl']

#DODGECOIN
dogeDolar = dados['dogecoin']['usd']
dogeReal = dados['dogecoin']['brl']
