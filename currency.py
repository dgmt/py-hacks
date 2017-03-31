import datetime
import ujson as json

import requests
from pymongo import MongoClient
import telegram

import config


def main():
    c = MongoClient(config.MONGO_STRING)
    db = c[config.DB_NAME]
    coll = db[config.CURRENCY_MONGO_COLLECTION]

    resp = requests.get(config.ADDRESS)
    resp_obj = json.loads(resp.text)
    today = {
        "date": datetime.datetime.now(),
        "eur_mid": resp_obj["result"]["eur"]["sre"]
    }
    iid = coll.insert_one(today).inserted_id

    din_pay = config.PAYCHECK * float(today["eur_mid"])

    tommorrow = datetime.date.today() + datetime.timedelta(days=1)

    if tommorrow.day == 1:
        msg_text = config.REPORT_MSG.replace(
            '[[eur]]', today['eur_mid']).replace('[[paycheck]]', str(din_pay))
        bot = telegram.Bot(token=config.TELEGRAM_TOKEN)
        # bot.getMe()
        chat_id = bot.getUpdates()[-1].message.chat_id
        bot.sendMessage(chat_id=chat_id, text=msg_text)


if __name__ == '__main__':
    main()
