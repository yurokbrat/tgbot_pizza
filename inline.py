from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
import os
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bott = Bot(token='6029713105:AAEwBfAFBPxj08c-rpXikj9TEieJoQXtN_Q')
dp = Dispatcher(bott)

ans = dict()
#Кнопка-ссылка

urlkb = InlineKeyboardMarkup(row_width=2)
urlButton1=InlineKeyboardButton(text='Ссылка на ютуб', url='https://youtube.com')
urlButton2 = InlineKeyboardButton(text='Ссылка на гугл', url='https://google.com')
x = [InlineKeyboardButton(text='Ссылка на vk', url='https://vk.com'),\
     InlineKeyboardButton(text='Ссылка на aboba', url='https://aboba.com'),
     InlineKeyboardButton(text='Ссылка на facebook', url='https://facebook.com')]
urlkb.add(urlButton1,urlButton2).row(*x).\
    insert(InlineKeyboardButton(text='Ссылка на facebook2', url='https://facebook.com'))

@dp.message_handler(commands='Ссылки')
async def url_command(message: types.Message):
    await message.answer('Ссылки:',reply_markup=urlkb)
inklib = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='👍🏻',callback_data='like_1'),\
                                               InlineKeyboardButton(text='👎🏻',callback_data='like_-1'))


@dp.message_handler(commands='test')
async def test_commands(message: types.Message):
    await message.answer('Вам нравится наша пица?',reply_markup=inklib)

@dp.callback_query_handler(Text(startswith='like_'))
async def www_call(callback: types.CallbackQuery):
    res = int(callback.data.split('_')[1])
    if f'{callback.from_user.id}' not in ans:
        ans[f'{callback.from_user.id}'] = res
        await callback.answer('Вы проголосовали')
    else:
        await callback.answer('Вы уже проголосовали',show_alert=True)
executor.start_polling(dp,skip_updates=True)