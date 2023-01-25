import requests


def get_info_zipcode(zipcode):
    url_base = f"https://viacep.com.br/ws/{zipcode}/json/"
    resq = requests.get(url_base)
    if resq.status_code == 200:
        d = resq.json()
    else:
        return "Error"


def get_info_logradouro(zipcode):
    url_base = f"https://viacep.com.br/ws/{zipcode}/json/"
    resq = requests.get(url_base)
    if resq.status_code == 200:
        d = resq.json()
    else:
        return "Error"
    return d['logradouro']


def get_info_city(zipcode):
    url_base = f"https://viacep.com.br/ws/{zipcode}/json/"
    resq = requests.get(url_base)
    if resq.status_code == 200:
        d = resq.json()
    else:
        return "Error"
    return d['localidade']


def get_info_uf(zipcode):
    url_base = f"https://viacep.com.br/ws/{zipcode}/json/"
    resq = requests.get(url_base)
    if resq.status_code == 200:
        d = resq.json()
    else:
        return "Error"
    return d['uf']


def get_info_ibge(zipcode):
    url_base = f"https://viacep.com.br/ws/{zipcode}/json/"
    resq = requests.get(url_base)
    if resq.status_code == 200:
        d = resq.json()
    else:
        return "Error"
    return d['ibge']


def get_info_gia(zipcode):
    url_base = f"https://viacep.com.br/ws/{zipcode}/json/"
    resq = requests.get(url_base)
    if resq.status_code == 200:
        d = resq.json()
    else:
        return "Error"
    return d['gia']


def get_info_ddd(zipcode):
    url_base = f"https://viacep.com.br/ws/{zipcode}/json/"
    resq = requests.get(url_base)
    if resq.status_code == 200:
        d = resq.json()
    else:
        return "Error"
    return d['ddd']


def get_info_siafi(zipcode):
    url_base = f"https://viacep.com.br/ws/{zipcode}/json/"
    resq = requests.get(url_base)
    if resq.status_code == 200:
        d = resq.json()
    else:
        return "Error"
    return d['siafi']


def get_info_complemento(zipcode):
    url_base = f"https://viacep.com.br/ws/{zipcode}/json/"
    resq = requests.get(url_base)
    if resq.status_code == 200:
        d = resq.json()
    else:
        return "Error"
    return d['complemento']


def get_info_bairro(zipcode):
    url_base = f"https://viacep.com.br/ws/{zipcode}/json/"
    resq = requests.get(url_base)
    if resq.status_code == 200:
        d = resq.json()
    else:
        return "Error"
    return d['bairro']


def get_info_cep(zipcode):
    url_base = f"https://viacep.com.br/ws/{zipcode}/json/"
    resq = requests.get(url_base)
    if resq.status_code == 200:
        d = resq.json()
    else:
        return "Error"
    return d['cep']


zipcode = input('Digite o CEP: ')
print(f"CEP: {get_info_cep(zipcode)}")
print(f"Logradouro: {get_info_logradouro(zipcode)}")
print(f"Complemento: {get_info_complemento(zipcode)}")
print(f"Bairro: {get_info_bairro(zipcode)}")
print(f"Cidade: {get_info_city(zipcode)}")
print(f"UF: {get_info_uf(zipcode)}")
print(f"DDD da Cidade: {get_info_ddd(zipcode)}")
print(f"IBGE: {get_info_ibge(zipcode)}")
print(f"GIA: {get_info_gia(zipcode)}")
print(f"Siafi: {get_info_siafi(zipcode)}")
