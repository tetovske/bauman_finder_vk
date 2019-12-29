import vk_api
import random
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

def send_message(sess, user, message):
    print("Ответ отправлен")
    sess.messages.send(user_id=user, message=message)

def listen_messages(bot):
    for event in pool.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            bot.method("messages.send", {"user_id": event.object["message"]["from_id"], "message": "Хаай", "random_id": 0})
    

token = ""
group_id = 156845414

bot = vk_api.VkApi(token=token)
bot._auth_token()
bot.get_api()
pool = VkBotLongPoll(bot, group_id, 1)
listen_messages(bot)


    

    
