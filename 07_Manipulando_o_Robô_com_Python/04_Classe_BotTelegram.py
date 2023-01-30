import requests
import time


class TelegramBot:

    def __init__(self):
        token = ""
        self.url_base = f"https://api.telegram.org/bot{token}/"

    def Start(self):
        update_id = None
        while True:
            updates = self.get_updates()

            data = updates["result"]
            print(data)

            pdate_id = data[-1]["update_id"]
            # print(f"update_id: {update_id}")

            message = str(data[-1]["message"]["text"])
            chat_id = data[-1]["message"]["from"]["id"]
            name = data[-1]["message"]["from"]["first_name"]

            print(f"Chat ID: {chat_id}")
            print(f"Message: {message}")

            self.reply("Hello! " + name + " my name is Robot Telegram!", chat_id)

            print("--------------------------------")
            time.sleep(5)

    def reply(self, answer, chat_id):
        link_request = f"{self.url_base}sendMessage?chat_id={chat_id}&text={answer}"
        requests.get(link_request)

    def get_updates(self):
        link_api = self.url_base + "getUpdates"
        r = requests.get(link_api)
        return r.json()


t = TelegramBot()
t.Start()
