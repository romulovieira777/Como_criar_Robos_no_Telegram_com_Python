import requests


def get_info_movie(title, year=None):
    url_base = f'http://www.omdbapi.com/?t={title}&y={year}&apikey=7c1c2d2a'
    resq = requests.get(url_base)
    if resq.status_code == 200:
        return resq.json()
    else:
        return "Error"


print(get_info_movie('The Matrix', 1999))
