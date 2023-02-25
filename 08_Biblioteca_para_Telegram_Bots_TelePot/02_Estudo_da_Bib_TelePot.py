import telepot
from pprint import pprint


token = ''

bot = telepot.Bot(token)

response = bot.getUpdates()

pprint(response)


resp = bot.sendMessage(id, 'Olá, Mundo!')
