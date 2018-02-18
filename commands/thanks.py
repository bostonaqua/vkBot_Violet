import command_system
from random import choice


def thank():
    rprhase = ['Всегда пожалуйста!',
               'Рада служить Вам!',
               'Автозаписывающие куклы рады услужить.',
               'Не стоит благодарностей. Это моя работа.',
               'Всегда рада помочь!']
    message = choice(rprhase)
    return message, ''


info_command = command_system.Command()

info_command.keys = ['спасибо', 'благодарю',
                     'благодарствую', 'ty']
info_command.desciption = 'Ответ на благодарствие'
info_command.process = thank
