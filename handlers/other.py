from aiogram import types, Dispatcher
from create_bot import dp
from create_bot import bot
import json
import string


# @dp.message_handler()
async def echo(message: types.Message):
    if message.text == "hello":
        await bot.send_message(message.from_user.id, f'{message.text} how are you {message.from_user.first_name} ?')
    else:
        await bot.send_message(message.from_user.id, message.text)
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(" ")}\
            .intersection(set(json.load(open('cens.json')))) != set():
        await message.reply('censored!!!')
        await message.delete()


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo)
