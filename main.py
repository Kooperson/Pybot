import logging

import aiogram

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

from config import TOKEN

API_TOKEN = TOKEN
import keyboard

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(regexp='(^cat[s]?$|^puss[y]?$)')
async def cats(message: types.Message):
    with open('data/cats.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Cats are here 😺')


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет, я бот Фифо", reply_markup=keyboard.greet_kb)


@dp.message_handler(Text(equals='Привет'))
async def echo(message: types.Message):
    await message.answer("Привет!", reply_markup = keyboard.ReplyKeyboardRemove())

@dp.message_handler()
async def echo(message : types.Message):
    print(message.text)
    if message.text == 'test' :
        await  message.reply("bip-bop")
    if message.text == '👋' :
        await  message.reply("🙃")
    else:
        await message.answer('What?')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
