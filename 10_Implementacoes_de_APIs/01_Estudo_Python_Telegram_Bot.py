import telegram
import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = ""

updater = Updater(token=TOKEN, use_context=True)

dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


def cep(update, context):
    cep_ = context.args
    cep_ok = cep_[0]

    if len(cep_ok) == 8:
        url_base = f"https://viacep.com.br/ws/{cep_ok}/json/"
        r = requests.get(url_base).json()
    else:
        r = {'logradouro': 'CEP inválido'}

    context.bot.send_message(chat_id=update.effective_chat.id, text=r['logradouro'])


def cot(update, context):
    ativo = context.args[0]

    url_base = f"https://www.mercadobitcoin.net/api/{ativo}/ticker/"

    r = requests.get(url_base).json()

    context.bot.send_message(chat_id=update.effective_chat.id, text=str(r))


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)

cep_handler = CommandHandler('cep', cep)
dispatcher.add_handler(cep_handler)

cot_handler = CommandHandler('cot', cot)
dispatcher.add_handler(cot_handler)

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

updater.start_polling()
