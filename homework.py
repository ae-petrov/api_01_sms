import os
import requests
import time

from dotenv import load_dotenv
from twilio.rest import Client


load_dotenv()
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
#NUMBER_FROM = os.getenv("NUMBER_FROM") тесты на практикуме пропускают только с конкретным указанным номером
#NUMBER_TO = os.getenv("NUMBER_TO") тесты на практикуме пропускают только с конкретным указанным номером

def get_status(user_id):
    
    url = 'https://api.vk.com/method/users.get'

    params = {"user_ids": user_id,
              "access_token": ACCESS_TOKEN,
              "v": '5.92',
              "fields": "online"
    }
    response = requests.post(url, params = params)
    try:
        data = response.json()["response"][0]
    except:
        print("Произошла ошибка при интерпретации результата")

    return data["online"]


def sms_sender(sms_text):

    client = Client(ACCOUNT_SID, AUTH_TOKEN)

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