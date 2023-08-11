import sqlite3 as sq
from create_bot import bot
from aiogram import types, Dispatcher


def sql_start():
    global base, cur
    base = sq.connect('crash_bandicoot.db')
    cur = base.cursor()
    if base:
        print("Database connected")
        base.execute(
            'CREATE TABLE IF NOT EXISTS main_series(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
        base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO main_series VALUES (?, ?, ?, ?)',
                    tuple(data.values()))
        base.commit()


async def sql_read(message: types.message):
    for ret in cur.execute('SELECT * FROM main_series').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'\n{ret[1]}\n\nDescription : {ret[2]} \n\nPrice : {ret[3]} $')
