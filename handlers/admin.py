from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram import types, Dispatcher
from create_bot import dp, bot
from data_base import sqlite_db
from keyboards import admin_kb
ID = None


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


async def moderator(message: types.message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'how can i assist my moderator today ?', reply_markup=admin_kb.button_case_admin)
    await message.delete()

# @dp.message_handler(commands='upload', state=None)


async def upload(message: types.Message):
    if message.from_user.id == ID:
        await FSMAdmin.photo.set()
        await message.reply('upload photo')
    else:
        await message.reply('you are not moderator !')
        await message.delete()


async def cancel_handler(message: types.message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('upload canceled successfully.')
    else:
        await message.reply("You're not moderator !")
        await message.delete()


async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
            await FSMAdmin.next()
            await message.reply('Enter the name ...')


# @dp.message_handler(state=FSMadmin.name)
async def load_name(message: types.message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
            await FSMAdmin.next()
            await message.reply('Enter the description ...')


# @dp.message_handler(state=FSMadmin.description)
async def load_description(message: types.message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
            await FSMAdmin.next()
            await message.reply('Enter the price ...')


# @dp.message_handler(state=FSMadmin.price)
async def load_price(message: types.message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price'] = float(message.text)
            await message.reply('You have successfully added item on listing.')
        await sqlite_db.sql_add_command(state)
        await state.finish()


async def empty(message: types.message):
    await bot.send_message(message.from_user.id, 'There is not command like this!!!')
    await message.delete()


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(upload, commands=['upload'], state=None)
    dp.register_message_handler(cancel_handler, Text(
        equals='cancel', ignore_case=True), state='*')
    dp.register_message_handler(moderator, commands=['moderator'])
    dp.register_message_handler(load_photo, content_types=[
                                'photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(cancel_handler, commands=['cancel'], state='*')
    dp.register_message_handler(empty)
