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

            update_id = data[0]["update_id"]
            print(f"update_id: {update_id}")

            message = str(data[-1]["message"]["text"])
            chat_id = data[0]["message"]["from"]["id"]
            print(f"chat_id: {chat_id}")
            print(f"message: {message}")

            print("--------------------------------")
            time.sleep(5)

    def get_updates(self):
        link_api = self.url_base + "getUpdates"
        r = requests.get(link_api)
        return r.json()


t = TelegramBot()
t.Start()
