import requests

zipcode = input('Digite o CEP: ')
if zipcode.replace('-', '') and len(zipcode) < 9:
    url_base = f"https://viacep.com.br/ws/{zipcode}/json/"
    resq = requests.get(url_base)
    if resq.status_code == 200:
        d = resq.json()
    else:
        print("Erro")
else:
    print("CEP inválido")


def get_info_logradouro():
    return d['logradouro']


def get_info_city():
    return d['localidade']


def get_info_uf():
    return d['uf']


def get_info_ibge():
    return d['ibge']


def get_info_gia():
    return d['gia']


def get_info_ddd():
    return d['ddd']


def get_info_siafi():
    return d['siafi']


def get_info_complemento():
    return d['complemento']


def get_info_bairro():
    return d['bairro']


def get_info_cep():
    return d['cep']


print(f"CEP: {get_info_cep()}")
print(f"Logradouro: {get_info_logradouro()}")
print(f"Complemento: {get_info_complemento()}")
print(f"Bairro: {get_info_bairro()}")
print(f"Cidade: {get_info_city()}")
print(f"UF: {get_info_uf()}")
print(f"DDD da Cidade: {get_info_ddd()}")
print(f"IBGE: {get_info_ibge()}")
print(f"GIA: {get_info_gia()}")
print(f"Siafi: {get_info_siafi()}")
