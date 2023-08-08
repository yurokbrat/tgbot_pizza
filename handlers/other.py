import json, string
from aiogram import types, Dispatcher
from create_bot import dp


# @dp.message_handler()
async def ban_send(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')} \
            .intersection(set(json.load(open('cenzor.json')))) != set():
        await(message.reply('Не ругайтесь матом и ведите себя культурно!'))
        await message.delete()


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(ban_send)
