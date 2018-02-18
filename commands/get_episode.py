import command_system
import vkapi


def get_episode(episode):
    attachment = vkapi.get_video_episode(-160242252, episode)
    message = ''
    return message, attachment


violet_command = command_system.Command()

violet_command.keys = ['[0-9]{1,2}(.{1,2})? сери[юя]']
violet_command.description = 'Пришлю серию с нашей озвучкой'
violet_command.process = get_episode
