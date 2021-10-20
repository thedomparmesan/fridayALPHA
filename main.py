import Constants as keys
from telegram.ext import *

import Response as R
import os

def handle_message(update, context):
    text = str(update.message.text).lower()
    user = update.message.from_user
    print(user['id'])
    with open('id.txt', 'w') as file:
        file.writelines(str(user['id']))
    with open('usrnm.txt', 'w') as file:
        file.writelines(str(user['first_name']))
    if user['id'] == 1736286395:
        response = R.sample_responses(text)
    elif user['id'] != 1736286395:
        with open('usrlist.txt', 'r') as file:
            usr = file.read()
        if str(user['id']) in usr:
            inpath = 'usrdata' + str(user['id']) + ".txt"
            compath = 'usrfin' + str(user['id']) + ".txt"
            if not os.path.exists(inpath):
                with open(inpath, 'x') as file:
                    file.writelines(" Q: Hello, I am Steven's friend A: Okay ")
                    response = R.sample_responses1(text)
            if os.path.exists(inpath):
                response = R.sample_responses1(text)
        if str(user['id']) not in usr:
            with open('usrlist.txt', 'a+') as file:
                grrp = (str(user['id']), ', ')
                file.writelines()
            inpath = 'usrdata' + str(user['id']) + ".txt"
            compath = 'usrfin' + str(user['id']) + ".txt"
            if os.path.exists(inpath):
                response = R.sample_responses1(text)
            if not os.path.exists(inpath):
                with open(inpath, 'x') as file:
                    file.writelines("Q: Hello, I am Steven's friend A: Okay ")
                response = R.sample_responses1(text)
    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()
