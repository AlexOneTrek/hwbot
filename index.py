from keyboard import keyboard, admin_keyboard
from connect import *

print("START")

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        response = event.object.text.lower()
        if event.object.peer_id != event.object.from_id:
            if response == "начать":
                vk_con.method('messages.send', {
                    'peer_id': event.object.peer_id,
                    'message': 'Я могу: \n 1) отправить вам ДЗ \n 2) отправить вам мем',
                    'random_id': 0,
                    'keyboard': keyboard
                })

            if response == 'пук':
                vk_con.method('messages.send', {
                    'peer_id': event.object.peer_id,
                    'message': 'обосрался.',
                    'random_id': 0,
                })

            if 'payload' in event.object:
                payloads = eval(event.object.payload)['button']
                print(payloads)
                if payloads == '1':
                    vk_con.method('messages.send', {
                        'peer_id': event.object.peer_id,
                        'message': '*тут ДЗ*',
                        'random_id': 0
                        })
                    print(payloads)

                elif payloads == '2':
                    vk_con.method('messages.send', {
                        'peer_id': event.object.peer_id,
                        'message': '*тут МЕМ*',
                        'random_id': 0
                    })
                    print(payloads)

        elif event.object.peer_id == event.object.from_id:
            if response == "тест":
                vk_con.method('messages.send', {
                    'peer_id': event.object.from_id,
                    'message': 'Я могу: \n 1) отправить вам ДЗ \n 2) отправить вам мем',
                    'random_id': 0,
                    'keyboard': admin_keyboard
                })

            elif response == "отправить домашнее задание":

                vk_con.method('messages.send', {
                    'peer_id': event.object.from_id,
                    'message': '*тут ДЗ*',
                    'random_id': 0
                })

            if event.object.from_id == 215453162:
                if response == 'админ':
                    vk_con.method('messages.send', {
                        'peer_id': event.object.from_id,
                        'message': 'Админка может: \n 1) Добавить ДЗ \n 2) Добавить мем',
                        'random_id': 0,
                        'keyboard': keyboard
                    })

            else:
                vk_con.method('messages.send', {
                    'peer_id': event.object.from_id,
                    'message': 'Извините, я вас не понял!',
                    'random_id': 0
                })

