from aiogram import types, Dispatcher
from create_bot import dp
from create_bot import bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db


async def command_start(message: types.message):
    try:
        await bot.send_message(message.from_user.id, f'Hello {message.from_user.first_name}', reply_markup=kb_client)
        await bot.send_message(message.from_user.id, 'Bot started successfully!')
        await message.delete()
    except:
        await message.reply("send message directly to the bot \nhttps://t.me/bandicootcrash_bot")


# @dp.message_handler(commands=['version'])
async def version(message: types.message):
    await bot.send_message(message.from_user.id, 'crash bandicoot 1.0')


# @dp.message_handler(commands=['main_series'])
async def games(message: types.message):
    await bot.send_message(message.from_user.id, 'crash bandicoot')
    await bot.send_message(message.from_user.id, 'crash bandicoot 2: Cortex Strikes Back')
    await bot.send_message(message.from_user.id, 'crash bandicoot: Warped')
    await bot.send_message(message.from_user.id, 'crash bandicoot: The Wrath of Cortex')
    await bot.send_message(message.from_user.id, 'Crash Twinsanity')
    await bot.send_message(message.from_user.id, 'Crash: Mind over Mutant')
    await bot.send_message(message.from_user.id, 'Crash Bandicoot 4: It\'s About Time')


# @dp.message_handler(commands=['racing'])
async def racing(message: types.message):
    await bot.send_message(message.from_user.id, 'Crash Team Racing')
    await bot.send_message(message.from_user.id, 'Crash Nitro Kart')
    await bot.send_message(message.from_user.id, 'Crash Tag Team Racing')
    await bot.send_message(message.from_user.id, 'Crash Team Racing Nitro-Fueled')


# @dp.message_handler(commands=['party'])
async def party(message: types.message):
    await bot.send_message(message.from_user.id, 'Crash Bash')
    await bot.send_message(message.from_user.id, 'Crash Boom Bang')
    await bot.send_message(message.from_user.id, 'Crash Team RUmble')


# @dp.message_handler(commands=['spin_off'])
async def spin_off(message: types.message):
    await bot.send_message(message.from_user.id, 'Crash Bandicoot: The Huge Adventure')
    await bot.send_message(message.from_user.id, 'Crash Bandicoot 2: N-Tranced')
    await bot.send_message(message.from_user.id, 'Crash Bandicoot Purple: Ripto\'s Rampage')
    await bot.send_message(message.from_user.id, 'Skylanders: Imaginators')


async def quit_kb(message: types.message):
    await bot.send_message(message.from_user.id, 'keyboard client removed', reply_markup=ReplyKeyboardRemove())


async def crash(message: types.message):
    await bot.send_message(message.from_user.id, 'Crash Bandicoot is a video game series created by Andy Gavin and Jason Rubin. It is published by Activision, Sierra Entertainment, Vivendi Universal Games, Konami, Universal Interactive Studios, King, and Sony Computer Entertainment, with entries developed by Polarbit, Toys for Bob, Beenox, Radical Entertainment, Vicarious Visions, Traveller\'s Tales, Eurocom, King and Naughty Dog.')


async def main_series(message):
    await sqlite_db.sql_read(message)
    await bot.send_message(message.from_user.id, 'All three in one game is available on playstation store as Crash Bandicoot™ N. Sane Trilogy for 39.99 $\nhttps://store.playstation.com/en-us/product/UP0002-CUSA07402_00-CRASHNSANETRLOGY')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(version, commands=['version'])
    dp.register_message_handler(racing, commands=['racing'])
    dp.register_message_handler(party, commands=['party'])
    dp.register_message_handler(spin_off, commands=['spin_off'])
    dp.register_message_handler(quit_kb, commands=['quit'])
    dp.register_message_handler(crash, lambda message: any(
        keyword in message.text for keyword in ['crash', 'coco', 'bandicoot']))
    dp.register_message_handler(main_series, commands=['main_series'])
