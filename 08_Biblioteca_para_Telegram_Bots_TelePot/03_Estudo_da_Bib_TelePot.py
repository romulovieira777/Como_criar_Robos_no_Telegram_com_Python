import time
import telepot
from pprint import pprint
from telepot.loop import MessageLoop

token = ''

bot = telepot.Bot(token)


# def handle(msg):
#     pprint(msg)
#
#
# MessageLoop(bot, handle).run_as_thread()
# print('Listening ...')


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        bot.sendMessage(chat_id, msg['text'])

    if content_type == 'audio':
        bot.sendMessage(chat_id, 'Audio recebido')


bot = telepot.Bot(token)
MessageLoop(bot, handle).run_as_thread()
pprint('Listening ...')


# Keep the program running.
while 1:
    time.sleep(10)
