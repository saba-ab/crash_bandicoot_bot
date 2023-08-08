from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/start')
b2 = KeyboardButton('/version')
b3 = KeyboardButton('/main_series')
b4 = KeyboardButton('/racing')
b5 = KeyboardButton('/party')
b6 = KeyboardButton('/spin_off')
b7 = KeyboardButton('send number', request_contact=True)
b8 = KeyboardButton('send location', request_location=True)
b9 = KeyboardButton('/quit')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(b1).insert(b3).row(b6, b7, b8, b9)
