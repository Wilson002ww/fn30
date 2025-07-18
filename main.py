from telebot import TeleBot
from telebot.types import Message
from buttons import menu

TOKEN='8017381723:AAEKB78sAYh3CGgRE-eFN-IcrGeHBbv3O4o'

bot=TeleBot(TOKEN)
@bot.message_handler(commands=["/start"])
def reaction_to_start(message:Message):
    chat_id=message.chat.id
    bot.send_message(chat_id,f"Hello!",
                     reply_markup=menu())



@bot.message_handler(commands=["/help"])
def reaction_to_start(message:Message):
    chat_id=message.chat.id
    bot.send_message(chat_id,f"Siz yordam uchun adminga murojat qilishingiz mumkun!\n"
                             f"adminga yozish uchun /admin komandasini yozing")


@bot.message_handler(commands=["/admin"])
def reaction_to_start(message:Message):
    chat_id=message.chat.id
    bot.send_message(chat_id,f"@User0242")


if __name__=="__main__":
    bot.infinity_polling()