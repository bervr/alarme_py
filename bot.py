# pip install requests
# pip install pytelegrambotapi
import telebot
import config
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Привет', 'Пока')

keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
keyboard2.row('?', 'Пока', 'назад')
global admin_list, is_admin
is_admin = False
# with open('config.py', encoding = 'utf-8') as f:
#     api_key = f.read()
#print(api_key)

with open('.admins', encoding = 'utf-8') as f:
    admin_list = int(f.read())



bot = telebot.TeleBot(config.token)
@bot.message_handler(commands=['start'])

def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start',reply_markup=keyboard1)



@bot.message_handler(content_types=['text'])
def send_text(message):
    print(message.text)
    if admin_list != message.from_user.id:
        if message.text.lower() == 'привет':
            bot.send_message(message.chat.id, 'Привет, незнакомец')
        elif message.text.lower()  == 'пока':
            bot.send_message(message.chat.id, 'Прощай, незнакомец')
        elif message.text.lower() == '?':
            bot.send_message(message.chat.id, 'Ю хев ноу райтс то ватч зы страрз')
        else:
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMUXxArpiyac3IUz5Tfy0BWUwwhF7sAAi8AA0vQuxA9O2awSYy0bxoE')
    else:
       if message.text.lower() == 'привет':
           bot.send_message(message.chat.id, 'Привет, хозяин')
       elif message.text.lower() == 'пока':
           bot.send_message(message.chat.id, 'Прощай, хозяин')
       elif message.text.lower() == '?':
           bot.send_message(message.chat.id, 'Я обязательно узнаю', reply_markup=keyboard2)
       elif message.text.lower() == 'Назад':
           bot.send_message(message.chat.id, '', reply_markup=keyboard1)
       else:
           bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMvXxAvx--9IXS2tOp4SiH2-TskTx0AAl0FAAIqVRgCyA2v9Dv1ThYaBA')

@bot.message_handler(content_types=['sticker'])
def send_stiker_id(message):
    print(message.sticker.file_id)


if __name__ == '__main__':
    bot.polling()