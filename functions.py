"""
Module with functions
"""

import товар as tvr

import messages as msg

PATH = 'users.txt'


PATH2 = 'tvr.txt'

def buy_fnctn():
    file = open(PATH2, mode='r')
    array_file = (file.read()).splitlines()
    #print(array_file)
    arr2 = ''.join(array_file)
    arr3 = arr2.split(', ')
    new_final_list = []
    for i in arr3:
        x = i.split(" ")
        new_final_list.append(x)
    #print(new_final_list)


def start(update, context):
    chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    text = msg.start.format(first_name)
    context.bot.send_message(chat_id=chat_id,
                             text=text)
    f = open(PATH, 'a')
    f.write(update.message.from_user.username + '\n')


def text_msg(update, context):
    chat_id = update.message.chat_id
    text = update.message.text.lower()
    smv = ['самовар', 'самавар', 'сомовар']
    coca = ['кокакола', 'кола', 'колу', 'кокаколу', 'коку', 'кока']
    tel = ['телефон', 'телифон', 'тилифон', 'тилефон', 'тел']
    if text in smv:
        context.bot.send_message(chat_id=chat_id,
                                 text=msg.samovar)
    elif text in coca:
        context.bot.send_message(chat_id=chat_id,
                                 text=msg.cola)

    elif text in tel:
        context.bot.send_message(chat_id=chat_id,
                                 text=msg.telefon)
