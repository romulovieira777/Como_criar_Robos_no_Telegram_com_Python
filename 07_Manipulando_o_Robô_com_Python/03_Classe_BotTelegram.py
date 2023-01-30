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
            print(updates)

            print("--------------------------------")
            time.sleep(5)

    def get_updates(self):
        link_api = self.url_base + "getMe"
        r = requests.get(link_api)
        return r.json()


t = TelegramBot()
t.Start()
