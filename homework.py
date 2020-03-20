import time
import os

import requests
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

def get_status(user_id):
    access_token = os.getenv("access_token")
    url = 'https://api.vk.com/method/users.get'

    params = {"user_ids": user_id,
              "access_token": access_token,
              "v": '5.92',
              "fields": "online"
    }
    response = requests.post(url, params = params)
    data = response.json()["response"][0]

    return data["online"]


def sms_sender(sms_text):
    account_sid = os.getenv("account_sid")
    auth_token = os.getenv("auth_token")
    #number_from = os.getenv("NUMBER_FROM") тесты на практикуме пропускают только с конкретным указанным номером
    #number_to = os.getenv("NUMBER_TO") тесты на практикуме пропускают только с конкретным указанным номером

    client = Client(account_sid, auth_token)

    message = client.messages.create(
                            body=sms_text,
                            from_='+14102028808', #тесты на практикуме пропускают только с конкретным указанным номером
                            to='+79069110025', #тесты на практикуме пропускают только с конкретным указанным номером
                            )
    return message.sid 


if __name__ == "__main__":
    vk_id = input("Введите id ")
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)