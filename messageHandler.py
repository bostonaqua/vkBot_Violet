import vkapi
import os
import importlib
import re
from command_system import command_list


def read_blacklist():
    with open('black.list', 'r') as f:
        listed = list(set(f.read().splitlines()))
    return listed


def write_blacklist(blacklist):
    with open('black.list', 'w') as f:
        for i in blacklist:
            f.write('{0}\n'.format(i))
    return


def addto_blacklist(userid):
    temp = []
    userid = str(userid)
    temp = read_blacklist()
    temp.append(userid)
    write_blacklist(temp)


def delfrom_blacklist(userid):
    temp = []
    userid = str(userid)
    temp = read_blacklist()
    temp.remove(userid)
    write_blacklist(temp)


def is_blacklisted(userid):
    listed = read_blacklist()
    for i in listed:
        if str(userid) == i:
            return True
    return False


def load_modules():
    files = os.listdir("commands")
    modules = filter(lambda x: x.endswith('.py'), files)
    for m in modules:
        importlib.import_module("commands." + m[0:-3])


def get_answer(body, userid):
    attachment = ''
    message = ''
    if 'отключить бота' in body:
        if is_blacklisted(userid):
            message = ''
            return message, attachment
        else:
            addto_blacklist(userid)
            message = ('Бот отключен!\nНапиши "Включить бота", '
                       'чтобы активировать меня снова.')
            return message, attachment
    if 'включить бота' in body:
        if is_blacklisted(userid):
            delfrom_blacklist(userid)
            message = 'Рада вновь с тобой пообщаться!'
            return message, attachment
        else:
            message = 'Я никуда не уходила=)'
            return message, attachment
    if not is_blacklisted(userid):
            # Сообщение по умолчанию если распознать не удастся
        message = ('Прости, я бот, и не все понимаю. Я еще учусь.\n'
                   'Напиши "Отключить бота", чтобы я тебе не мешала.\n'
                   'Напиши "Помощь", чтобы увидеть список доступных комманд.')
        for c in command_list:
            for b in c.keys:
                if b in body:
                    message, attachment = c.process()
                    return message, attachment
                else:
                    if re.search(b, body):
                        match = re.search(r'\d', body)
                        episode = match.group()
                        message, attachment = c.process(episode)
                        return message, attachment
    return message, attachment


def create_answer(data, token):
    load_modules()
    user_id = data['user_id']
    message, attachment = get_answer(data['body'].lower(), user_id)
    if (message, attachment):
        vkapi.send_message(user_id, token, message, attachment)
