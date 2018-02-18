import command_system


def hello():
    message = ('Привет, друг!\nЯ твоя автозаписывающая кукла!\n'
               'Отправь мне "Помощь", чтобы узнать доступные команды.')
    return message, ''


hello_command = command_system.Command()

hello_command.keys = ['привет', 'hello', 'дратути', 'здравствуй',
                      'здравствуйте', 'hi', 'хай', 'приветики',
                      'прив', 'хэлоу', 'ауе', 'здрасте']
hello_command.description = 'Приветствие'
hello_command.process = hello
