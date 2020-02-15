from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api

vk_con = vk_api.VkApi(token='faa5177ab9ea39bf73ada0ea48681992dde6be93109819569ab6179d082dd06d3a3b42293f01cffcf9dae')
vk_con._auth_token()
vk_con.get_api()
longpoll = VkBotLongPoll(vk_con, 153121303)