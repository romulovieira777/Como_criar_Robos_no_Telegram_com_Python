import requests


def get_ticks(moeda='BTC', metodo='ticker'):
    url_base = f'https://www.mercadobitcoin.net/api/{moeda}/{metodo}/'
    resq = requests.get(url_base)
    if resq.status_code == 200:
        return resq.json()
    else:
        return "Error"


d = get_ticks('ETH')
print(d)
