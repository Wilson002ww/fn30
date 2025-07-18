from telebot import TeleBot

TOKEN='8017381723:AAEKB78sAYh3CGgRE-eFN-IcrGeHBbv3O4o'

bot=TeleBot(TOKEN)

if __name__=="__main__":
    bot.infinity_polling()