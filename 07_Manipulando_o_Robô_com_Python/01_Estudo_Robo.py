import requests
import time

token = ""

url_base = f""


while True:
    r = requests.get(url_base + "/getUpdates")
    resposta_dict = r.json()
    print(resposta_dict)
    time.sleep(5)
