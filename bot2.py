#pip install aiogram
import logging
from datetime import datetime
from aiogram import Bot, Dispatcher, executor, types
logging.basicConfig(level=logging.INFO)
with open('config.py', encoding ='utf-8') as f:
    api_key = f.read()
bot = Bot(token=api_key)
dp = Dispatcher(bot)

def is_admin(id):
    with open('.admins', encoding='utf-8') as f:
        for i in f:
            if id == int(i):
                return True
        else:
            return False

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    print(message.from_user.id)
    if is_admin(int(message.from_user.id)):
        print(message.from_user.id, datetime.today())
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard= True)
        keyboard.add(types.KeyboardButton(text='проверка состояния'))
        keyboard.add(types.KeyboardButton(text='поставить на охрану'))
        keyboard.add(types.KeyboardButton(text='снять с охраны'))
        keyboard.add(types.KeyboardButton(text='перезагрузка'))
        keyboard.add(types.KeyboardButton(text='отмена'))
        await message.answer('приветствие',  reply_markup=keyboard)
    else:
        await message.answer_sticker('CAACAgIAAxkBAAMvXxAvx--9IXS2tOp4SiH2-TskTx0AAl0FAAIqVRgCyA2v9Dv1ThYaBA')

# Хэндлер на текстовое сообщение с текстом “Отмена”
@dp.message_handler(lambda message: message.text == "отмена")
async def action_cancel(message: types.Message):
    print(message.from_user.id)
    remove_keyboard = types.ReplyKeyboardRemove()
    await message.answer("Действие отменено. Введите /start, чтобы начать заново.", reply_markup=remove_keyboard)

# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.reply(message.text)
#     await message.answer("re-re")



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
