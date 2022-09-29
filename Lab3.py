# -*- coding: utf-8 -*-
# Напишите загрузчик файлов, используя потоки. Посмотрите описание библиотеки requests

import os
import random

import requests
from threading import Thread


def download(links):
    for i in range(len(links)):
        r = requests.get(links[i])
        out = open(str(random.randint(0, 15)) + ".jpg", "wb")
        out.write(r.content)
        out.close()


thread = Thread(target=download, kwargs=dict(
    links=['https://avatars.mds.yandex.net/i?id=4b811511a8bba918a9e8f74a65ffa76e-5233011-images-thumbs&n=13.jpg']))
thread.start()
download(links=['https://w-dog.ru/wallpapers/1/12/542097280410793/krasivaya-priroda-s-vodyanoj-melnicej.jpg'])
thread.join()