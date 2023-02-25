import time
import telepot
from pprint import pprint
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

token = ''

bot = telepot.Bot(token)


def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Aperte', callback_data='Feito'),
         InlineKeyboardButton(text='Sim', callback_data='Ok'),
         InlineKeyboardButton(text='Não', callback_data='No')],
    ])

    bot.sendMessage(chat_id, 'Escolha a opção abaixo', reply_markup=keyboard)


def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)

    pprint(msg)
    bot.answerCallbackQuery(query_id, text='Você escolheu: {}'.format(query_data))


MessageLoop(bot, {'chat': on_chat_message, 'callback_query': on_callback_query}).run_as_thread()

print('Listening ...')

while 1:
    time.sleep(10)
