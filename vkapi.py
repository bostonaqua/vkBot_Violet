import vk
from settings import ac_token
import random

session = vk.Session()
api = vk.API(session, v=5.0)


def send_message(user_id, token, message, attachment=""):
    api.messages.send(access_token=token, user_id=str(user_id),
                      message=message, attachment=attachment)


def get_random_wall_picture(group_id):
    max_num = api.photos.get(owner_id=group_id, album_id='wall',
                             count=0)['count']
    num = random.randint(1, max_num)
    photo = api.photos.get(owner_id=str(group_id), album_id='wall',
                           count=1, offset=num)['items'][0]['id']
    attachment = 'photo' + str(group_id) + '_' + str(photo)
    return attachment


def get_video_episode(group_id, episode):
    video = api.video.get(owner_id=group_id, album_id=int(episode),
                          count=2, access_token=ac_token)['items']
    for i in video:
        if 'vk.com' in str(i['player']):
            attachment = 'video' + str(i['owner_id']) + '_' + str(i['id'])
            return attachment
