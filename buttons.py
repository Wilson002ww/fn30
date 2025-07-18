from telebot.types import ReplyKeyboardMarkup,KeyboardButton

def menu():
    markup=ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    btn1=KeyboardButton('Fantastik')
    btn2=KeyboardButton("Xorror")
    btn3=KeyboardButton("Dramma")
    btn4=KeyboardButton("Boevik")
    btn5=KeyboardButton("detecktive ")
    markup.add(btn1,btn4,btn3,btn2,btn5)
    return markup