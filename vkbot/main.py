from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime

import random
import time

#login, password = "login", "password"
#vk_session = vk_api.VkApi(login, password)
#vk_session.auth()

token = "a894afae3e43b653c78b52f8e096108c8563fa61c272eeaf937635a571e807f296b5111b6e31c0e41f773"
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Сообщение пришло в: '+str(datetime.strftime(datetime.now(), "%H:%M:%S")))
            print('Текст сообщения: '+str(event.text))
            print(event.user_id)
            response = event.text.lower()
            if event.from_user and not (event.from_me):
                if response == "привет":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Иди нахуй!', 'random_id': 0})