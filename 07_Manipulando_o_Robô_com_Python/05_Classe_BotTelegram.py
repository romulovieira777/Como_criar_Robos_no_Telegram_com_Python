import requests
import time


class TelegramBot:

    def __init__(self):
        token = ""
        self.url_base = f"https://api.telegram.org/bot{token}/"

    def Start(self):
        update_id = None
        while True:
            find_zipcode = False

            updates = self.get_updates()
            data = updates["result"]
            chat_id = data[-1]["message"]["from"]["id"]
            self.reply("Enter the zip code to find the street.", chat_id)

            while True:
                updates = self.get_updates()
                data = updates["result"]

                pdate_id = data[-1]['update_id']

                message = str(data[-1]["message"]["text"])
                chat_id = data[-1]["message"]["from"]["id"]

                name = data[-1]["message"]["from"]["first_name"]

                if message and not(find_zipcode):
                    print("Waiting for zip code...")
                    if len(message) == 8:
                        print("Zip code Ok!")
                        c = self.get_info_zipcode(message)
                        self.reply("Your zip code is: " + c['cep'], chat_id)
                        self.reply("Your street is: " + c['logradouro'], chat_id)
                        self.reply("Your neighborhood is: " + c['bairro'], chat_id)
                        self.reply("Your city is: " + c['localidade'], chat_id)
                        self.reply("Your uf is: " + c['uf'], chat_id)
                        self.reply("Your dd is: " + c['ddd'], chat_id)
                        find_zipcode = True

                print('------------------------------------')

                time.sleep(5)

    def reply(self, answer, chat_id):
        link_request = f"{self.url_base}sendMessage?chat_id={chat_id}&text={answer}"
        requests.get(link_request)

    def get_updates(self):
        link_api = self.url_base + "getUpdates"
        r = requests.get(link_api)
        return r.json()

    def get_info_zipcode(self, zipcode):
        code = zipcode.replace('-', '')
        url_base = f"https://viacep.com.br/ws/{zipcode}/json/"
        resq = requests.get(url_base)
        if resq.status_code == 200:
            d = resq.json()
            return d


t = TelegramBot()
t.Start()
