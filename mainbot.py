import requests
from lxml import html


def pars():
    url = 'http://aniplay.tv/animes/violet-evergarden-rus'
    r = requests.get(url)
    pars = r.text
    tree = html.fromstring(pars)
    episode_list = tree.xpath('//table[@class="episodes-list"]')[0]
    lepisode = episode_list.xpath('.//td/text()')
    lst = ''
    for i in lepisode:
        if 'серия' in i:
            lst = lst + i.split('\r\n\t\t\t\t\t\t\t\t\t', 1)[1] + '\r\n'
    return lst
