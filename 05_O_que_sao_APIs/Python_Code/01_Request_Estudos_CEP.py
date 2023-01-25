import requests

resp = requests.get('https://viacep.com.br/ws/01001000/json/')
print(resp.status_code)
print(resp.text)
print(resp.json())


def get_info_zipcode(zipcode):
    url_base = f"https://viacep.com.br/ws/{zipcode}/json/"
    resq = requests.get(url_base)
    if resq.status_code == 200:
        return resq.json()
    else:
        return "Error"


d = get_info_zipcode('03805000')
print(d)
print(d['logradouro'])


def get_info_address(logradouro):
    return d['logradouro']


print(get_info_address(d))


def get_info_city(cidade):
    return d['localidade']


print(get_info_city(d))
