import json
import urllib.request
import time
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

token = ''

bot = telepot.Bot(token)


def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Rua', callback_data='logradouro'),
         InlineKeyboardButton(text='Estado', callback_data='uf'),
         InlineKeyboardButton(text='Bairro', callback_data='bairro')],
    ])

    bot.sendMessage(chat_id, 'Escolha a opção abaixo', reply_markup=keyboard)


def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)

    zipcode = get_info_cep("01001000")
    bot.answerCallbackQuery(query_id, text='Você escolheu: '+str(query_data) + " = " + zipcode[str(query_data)])


def get_info_cep(cep):
    url_base = f"https://viacep.com.br/ws/{cep}/json/"
    resp = urllib.request.urlopen(url_base)
    return json.loads(resp.read())


MessageLoop(bot, {'chat': on_chat_message, 'callback_query': on_callback_query}).run_as_thread()

print('Listening ...')

while 1:
    time.sleep(10)
