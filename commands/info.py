import mainbot
import command_system


def info():
    message = mainbot.pars()
    return message, ''


info_command = command_system.Command()

info_command.keys = ['список серий', 'названия серий',
                     'вышло серий', 'серий вышло']
info_command.desciption = 'Покажу список серий'
info_command.process = info
