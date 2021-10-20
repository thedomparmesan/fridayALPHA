from telegram.ext import *
import Constants as keys
import requests

import telegram


def sample_responses(input_text):
    print("Steven")
    user_message = input_text
    if user_message == "/start":
        return "Hello Sir"
    elif user_message != "/start":
        with open('data.txt', 'a+') as f:
            fil = ("Q: ", user_message, " ", "A: ")
            f.writelines(fil)

        with open('con.txt', 'r') as file:
            context = file.read()
        with open('data.txt', 'r') as file:
            convo = file.read()

        with open('fin.txt', 'w') as f:
            finl = context, convo
            f.writelines(finl)

        with open('fin.txt', 'r') as file:
            question = file.read()

        res = requests.post(
            "https://api.ai21.com/studio/v1/j1-large/complete",
            headers={"Authorization": "Bearer LvS1U98SI7T277JO35yX3XtoAWUogynd"},
            json={
                "prompt": question,
                "numResults": 1,
                "maxTokens": 100,
                "stopSequences": ["Q:"],
                "topKReturn": 0,
                "temperature": 0.3
            }
        )
        data = res.json()
        reply = data['completions'][0]['data']['text']
        with open('data.txt', 'a+') as f:
            f.writelines(reply)
        return reply

def sample_responses1(input_text):
    user_message = input_text
    with open('id.txt', 'r') as file:
        ussr = file.read()
    with open('usrnm.txt', 'r') as file:
        ussrnm = file.read()
    inpath = 'usrdata' + str(ussr) + ".txt"
    compath = 'usrfin' + str(ussr) + ".txt"
    print("Not Steven")
    print(str(ussr))
    msglist = ['tell', 'remind']

    if user_message == "/start":
        return "Please Identify yourself"
    elif user_message != "/start":
        if "tell" in user_message and "steven" in user_message or "remind" in user_message and "steven" in user_message or "tell" in user_message and "him" in user_message or "remind" in user_message and "him" in user_message:
            msgr = ["Hey, Steven. A person with the username of '", ussrnm,
                   "' has a messsage for you; ", """, user_message, "...", """]
            msg = ''.join(msgr)
            bot = telegram.Bot(token='2064996977:AAG96k4GcLLab_pk7ktHJaYNp8F41TF8i-k')
            bot.send_message(chat_id='1736286395', text=msg)
            return "Message has been sent"
        else:
            with open(inpath, 'a+') as f:
                fil = (" Q: ", user_message, ". ", "A: ")
                f.writelines(fil)

            with open('con2.txt', 'r') as file:
                context = file.read()
            with open(inpath, 'r') as file:
                convo = file.read()

            with open(compath, 'w') as f:
                finl = context,convo
                f.writelines(finl)

            with open(compath, 'r') as file:
                question = file.read().replace('\n', '')

            res = requests.post(
                "https://api.ai21.com/studio/v1/j1-large/complete",
                headers={"Authorization": "Bearer LvS1U98SI7T277JO35yX3XtoAWUogynd"},
                json={
                    "prompt": question,
                    "numResults": 1,
                    "maxTokens": 100,
                    "stopSequences": ["Q:"],
                    "topKReturn": 0,
                    "temperature": 0.1
                }
            )
            data = res.json()
            reply = data['completions'][0]['data']['text']
            print(reply)

            with open(inpath, 'a+') as f:
                f.writelines(reply)
            return reply
