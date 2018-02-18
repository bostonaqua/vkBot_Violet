import command_system
import vkapi


def violet():
    # Получаем случайную картинку из паблика
    attachment = vkapi.get_random_wall_picture(-160242252)
    message = 'Картинка со стены нашего паблика=)'
    return message, attachment


violet_command = command_system.Command()

violet_command.keys = ['violet', 'вайлет', 'эвергаден',
                       'эвергарден', 'evergarden', 'фото', 'картинку']
violet_command.description = 'Пришлю картинку с Вайлет'
violet_command.process = violet
