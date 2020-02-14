from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api
from keyboard import keyboard

vk_con = vk_api.VkApi(token='faa5177ab9ea39bf73ada0ea48681992dde6be93109819569ab6179d082dd06d3a3b42293f01cffcf9dae')
vk_con._auth_token()
vk_con.get_api()
longpoll = VkBotLongPoll(vk_con, 153121303)

print("START")

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        response = event.object.text.lower()
        payloads = event.object.payload
        if event.object.peer_id != event.object.from_id:
            if response == "начать":
                vk_con.method('messages.send', {
                    'peer_id': event.object.peer_id,
                    'message': 'Я могу: \n 1) отправить вам ДЗ \n 2) отправить вам мем',
                    'random_id': 0,
                    'keyboard': keyboard
                })
                print(payloads)
            elif payloads == '{"button":"1"}':
                vk_con.method('messages.send', {
                    'peer_id': event.object.peer_id,
                    'message': '*тут ДЗ*',
                    'random_id': 0
                })
                print(payloads)

            elif payloads == '{"button":"2"}':
                vk_con.method('messages.send', {
                    'peer_id': event.object.peer_id,
                    'message': '*тут МЕМ*',
                    'random_id': 0
                })
                print(payloads)

            else:
                vk_con.method('messages.send', {
                    'peer_id': event.object.peer_id,
                    'message': 'Извините, я вас не понял!',
                    'random_id': 0
                })
                print(payloads)
        elif event.object.peer_id == event.object.from_id:
            if response == "тест":
                vk_con.method('messages.send', {
                    'peer_id': event.object.from_id,
                    'message': 'Я могу: \n 1) отправить вам ДЗ \n 2) отправить вам мем',
                    'random_id': 0,
                    'keyboard': keyboard
                })

            elif response == "отправить домашнее задание":

                vk_con.method('messages.send', {
                    'peer_id': event.object.from_id,
                    'message': '*тут ДЗ*',
                    'random_id': 0
                })

            else:
                vk_con.method('messages.send', {
                    'peer_id': event.object.from_id,
                    'message': 'Извините, я вас не понял!',
                    'random_id': 0
                })
