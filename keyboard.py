from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup , KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_hi = KeyboardButton('Привет')
greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
greet_kb.add(button_hi)