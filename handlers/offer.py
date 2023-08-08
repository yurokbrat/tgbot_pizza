from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
from create_bot import dp, bott
from data_base import devilery_db
from keyboards import client_offer_keyb, kb_client

ID = None

off = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton('Оформить новый заказ🆕', callback_data='new_order'), \
                                            InlineKeyboardButton('Узнать статус заказа❔', callback_data='know_status'),
                                            InlineKeyboardButton('Отменить заказ❌', callback_data='cancel_order'), \
                                            InlineKeyboardButton('◀️Вернуться назад', callback_data='back'), \
                                            InlineKeyboardButton('Проверка', callback_data='test'))

back = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton('◀️Вернуться назад', callback_data='back'))
class FSMClient(StatesGroup):
    offer = State()
    name = State()
    phone = State()
    place = State()


class StateOrder(StatesGroup):
    wait_order = State()

async def keys2(callback: types.CallbackQuery):
    if callback.data == 'test':
        await bott.send_message(callback.from_user.id,'кнопка работает')
        await callback.answer()
    if callback.data == 'new_order':
        await bott.send_message(callback.from_user.id, f'Какой заказ оформить? '
                                                  f'\nдоделывается машина состояний '
                                                  f'\nпока не работает', reply_markup= back)
        await callback.answer()

    if callback.data == 'know_status':
        await bott.send_message(callback.from_user.id, 'Пока не работает, доделывается', reply_markup= back)
        await callback.answer()

    if callback.data == 'cancel_order':
        await bott.send_message(callback.from_user.id, 'Функция добавится позднее', reply_markup= back)
        await callback.answer()

    if callback.data == 'back':
        await bott.send_message(callback.from_user.id, 'Эта кнопка работает')
        await bott.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id,
                                             reply_markup=off)
        await callback.answer()
'''    
    await StateOrder.wait_order.set()


async def cancel_handler(message: types.Message, state=FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Операция отменилась успешно! ')


async def process_order_number(message: types.message, state: FSMContext):
    order_number = message.text
    await devilery_db.sql_read_status_command(order_number)
    await state.finish()



def register_handlers_client_offer(dp: Dispatcher):
    #dp.register_message_handler(hello_offer, commands=['Заказы'])
    dp.register_message_handler(new_offer, commands=['Оформить_новый_заказ'])
    dp.register_message_handler(read_status, commands=['Узнать_статус_заказа'])
    #dp.register_message_handler(cancel_handler, state='*', commands='Отмена')
    #dp.register_message_handler(cancel_handler, Text(equals='Отмена', ignore_case=True), state='*')
    dp.register_message_handler(delete_offer, commands=['Отменить_заказ'])
    dp.register_message_handler(close_key, commands=['Убрать_клавиатуру'])
    
'''
def register_handlers_client_offer(dp: Dispatcher):
    dp.register_callback_query_handler(keys2, lambda x: x.data)