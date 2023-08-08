from aiogram import types, Dispatcher, filters
from create_bot import dp, bott
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards import client_offer_keyb
from handlers import offer

#клавиатуры

ink = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton('Наш график работы🕓', callback_data='work_time'), \
                                            InlineKeyboardButton('Где нас найти?📍', callback_data='place'),
                                            InlineKeyboardButton('Меню пиццерии 🍽', callback_data='menu'), \
                                            InlineKeyboardButton('Наши акции🔥',callback_data='sale'), \
                                            InlineKeyboardButton('Действия с заказами🛒', callback_data='orders'), \
                                            InlineKeyboardButton('Связаться с поддержкой🛠️', callback_data='help'))

help_ink = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton('Вопросы по доставке🛵', callback_data='ask_delivery'), \
                                            InlineKeyboardButton('Вопросы по оплате💵', callback_data='ask_pay'),
                                            InlineKeyboardButton('Вопросы по акциям🎁', callback_data='ask_sale'), \
                                            InlineKeyboardButton('Вопросы по меню🍽️', callback_data='ask_menu'), \
                                            InlineKeyboardButton('Здесь нет моего вопроса💬', callback_data='other'), \
                                            InlineKeyboardButton('◀️Вернуться назад', callback_data='back_menu'))

off2 = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton('Оформить новый заказ🆕', callback_data='new_order'), \
                                            InlineKeyboardButton('Узнать статус заказа❔', callback_data='know_status'),
                                            InlineKeyboardButton('Отменить заказ❌', callback_data='cancel_order'), \
                                            InlineKeyboardButton('◀️Вернуться назад', callback_data='back_menu'))

back = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton('◀️Вернуться назад', callback_data='back'))

go_menu = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton('◀️Вернуться назад', callback_data='back_menu'))

call_help = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton('У меня остались вопросы🙋‍♂️', callback_data='call_operator'),
    InlineKeyboardButton('◀️Вернуться назад', callback_data='go_ask_menu'))

# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.message):
    # try:
    await bott.send_message(message.from_user.id, f' Здравствуйте,{message.from_user.first_name}! '
                                                  f'Это телеграмм-бот пиццерии "Пицца В Дом! '
                                                  f'Просматривайте наше меню, следите за акциями, '
                                                  f'отслеживайте заказ,'
                                                  f'связывайтесь с поддержкой, не выходя из Telegram!"',
                            reply_markup=ink)


# except:
# await message.reply('Для того, чтобы пользоваться ботом пиццерии, напишите ему в ЛС:'
# '\nhttps://t.me/pizza_dom_vrnbot')

async def keys(callback: types.CallbackQuery):

    # график работы

    if callback.data == 'work_time':
        await bott.send_message(callback.from_user.id, 'Мы открыты для вас по следующему графику:'
                                                       '\nПн 10:00 - 22:00\nВт 10:00 - 22:00\n'
                                                       'Ср 10:00 - 22:00\nЧт 10:00 - 22:00\n'
                                                       'Пт 10:00 - 23:30\n'
                                                       'Сб 10:00 - 23:30\nВс 10:00 - 23:30', reply_markup=go_menu)
        await callback.answer()

    #местоположение

    if callback.data == 'place':
        latitude = 51.6707
        longitude = 39.2088
        await bott.send_location(callback.message.chat.id, latitude, longitude)
        await bott.send_message(callback.from_user.id, 'Мы находимся по адресу:\n'
                                                       'г.Воронеж, пр. Революции, д. 20', reply_markup=go_menu)
        await callback.answer()

    #меню пиццерии

    if callback.data == 'menu':
        read = await sqlite_db.sql_read2()
        for ret in read:
            await bott.send_photo(callback.from_user.id, ret[0], f'{ret[1]}\n{ret[2]}\nЦена: {ret[-1]}₽')
        await bott.send_message(callback.from_user.id, 'Ожидайте новинок и следите за обновлениями нашего меню!',
                                reply_markup=go_menu)
        await callback.answer()

    #Акции пиццерии

    if callback.data == 'sale':
        await bott.send_message(callback.from_user.id, 'Благодарим за интерес к нашим особым предложениям! 🎉\n'
                                                       'Вот волшебные акции, которыми мы хотим порадовать вас:\n'
                                                       '🌟 "Друзья радости" - Приведи друга и получите оба '
                                                       'особенный бонус!\n'
                                                       '🎁 "Волшебный первый заказ" - Получите волшебную скидку на свой '
                                                       'первый заказ!\n'
                                                       '🚀 "Легкий самовывоз" - Оформите самовывоз и получите '
                                                       'дополнительную скидку!\n'
                                                       '🎂 "Сладкий день рождения" - Отмечайте день рождения с нами и '
                                                       'получите особенную скидку!\n'
                                                       'Благодарим за интерес к нашим акциям! Ждем вашего заказа и '
                                                       'желаем вам удивительных покупок! 🍕', reply_markup= go_menu)

#Действия с заказами(не доделано)

    if callback.data == 'orders':
        await bott.send_message(callback.from_user.id, f'{callback.from_user.first_name}, что бы вы хотели сделать?' \
                                , reply_markup=off2)

    if callback.data == 'new_order':
        await bott.send_message(callback.from_user.id, f'Какой заказ оформить? '
                                                           f'\nдоделывается машина состояний '
                                                           f'\nпока не работает', reply_markup=back)
        await callback.answer()

    if callback.data == 'know_status':
        await bott.send_message(callback.from_user.id, 'Пока не работает, доделывается', reply_markup=back)
        await callback.answer()

    if callback.data == 'cancel_order':
        await bott.send_message(callback.from_user.id, 'Функция добавится позднее', reply_markup=back)
        await callback.answer()


#Тех поддержка

    if callback.data == 'help':
        await bott.send_message(callback.from_user.id, f'{callback.from_user.first_name}, какой вопрос вас интересует?'\
                                , reply_markup=help_ink)
        await callback.answer()
    
    if callback.data == 'ask_delivery':
        with open('map.png', 'rb') as photo_file:
            await bott.send_photo(callback.from_user.id, photo_file)
        await bott.send_message(callback.from_user.id,
                                'В ЗЕЛЁНОЙ ЗОНЕ - заказы принимаются от 500 рублей (Стоимость доставки - 50 рублей). '
                                'Заказы от 700 рублей доставляются бесплатно.\n'
                                'В ОРАНЖЕВОЙ ЗОНЕ -  заказы принимаются от 800 рублей (Стоимость доставки - 100 рублей). '
                                'Заказы от 1000 рублей - доставляются бесплатно. \n'
                                'В СИНЕЙ ЗОНЕ -  заказы принимаются от 1000 рублей (Стоимость доставки - 100 рублей). '
                                'Заказы от 1500 рублей - доставляются бесплатно.', reply_markup=call_help)
        await callback.answer()

    if callback.data == 'ask_pay':
        await bott.send_message(callback.from_user.id, 'При заказе доставки пиццы необходимо выбрать удобный для Вас '
                                                       'способ оплаты. На данный момент мы можем предложить '
                                                       'Вам два варианта:\n'
                                                       '💵 Наличными курьеру\n'
                                                       '💳 По терминалу курьеру\n'
                                                       'Выберите удобный способ получения и оплаты заказа, а мы доставим'
                                                       ' пиццу быстро и качественно! 🍕🚀 ', reply_markup=call_help)
        await callback.answer()

    if callback.data == 'ask_sale':
        await bott.send_message(callback.from_user.id, 'Описание и условия наших акций, которыми мы рады поделиться:\n'
                                                       '🌟 "Друзья радости" - Приглашайте друзей заказать у нас и '
                                                       'получайте оба 10% бонус от стоимости каждого заказа.\n'
                                                       '🎁 "Волшебный первый заказ" - Новым клиентам 15% скидка на '
                                                       'первый заказ от 300 рублей.\n'
                                                       '🚀 "Легкий самовывоз" - При самовывозе 10% скидка на '
                                                       'любой заказ.\n'
                                                       '🎂 "Сладкий день рождения" - В день рождения 20% скидка при '
                                                       'заказе от 500 рублей (при предъявлении документа).\n'
                                                       'Ждем ваших заказов и желаем приятного аппетита! 🍕🎉',
                                reply_markup=call_help)
        await callback.answer()
    if callback.data == 'ask_menu':
        await bott.send_message(callback.from_user.id, 'Если у вас возникли вопросы по составам пиццы или хотите узнать '
                                                       'больше о наших ингредиентах, просто дайте нам знать. '
                                                       'Мы всегда готовы помочь с выбором и предоставить дополнительную '
                                                       'информацию по нашему меню. А также, будьте в курсе, что мы будем'
                                                       ' расширять ассортимент, и возможно, '
                                                       'скоро появятся новые интересные пиццы.', reply_markup=call_help)
        await callback.answer()
    if callback.data == 'other' or callback.data == 'call_operator':
        await bott.send_message(callback.from_user.id, 'Если у вас остались вопросы, на которые вы не нашли ответа, не '
                                                       'стесняйтесь позвонить нам! Наши приветливые сотрудники готовы '
                                                       'оперативно и понятно помочь вам, ответить на все ваши '
                                                       'интересующие вопросы и помочь решить любые возникшие вопросы! '
                                                       'Ваше удовлетворение - наш приоритет, и мы всегда рады быть '
                                                       'полезными для вас! Звоните прямо сейчас, и ждем ваших вопросов! '
                                                       '📞🤝\nНаш телефон: +7(915)555-55-55', reply_markup=go_menu)
        await callback.answer()
#возвращения в меню

    if callback.data == 'back_menu':
        await bott.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id,
                                             reply_markup=ink)
        await callback.answer()
    
    if callback.data == 'back_ask':
        await bott.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id,
                                             reply_markup=help_ink)
        await callback.answer()
        
    if callback.data == 'back':
        await bott.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id,
                                                 reply_markup=off2)
        await callback.answer()

    if callback.data == 'go_ask_menu':
        await bott.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id,
                                                 reply_markup=help_ink)
        await callback.answer()

# @dp.message_handler(commands=['Режим_работы'])
async def time_work_command(message: types.message):
    await bott.send_message(message.from_user.id, '\nПн 10:00 - 22:00\nВт 10:00 - 22:00\n'
                                                  'Ср 10:00 - 22:00\nЧт 10:00 - 22:00\n'
                                                  'Пт 10:00 - 23:30\n'
                                                  'Сб 10:00 - 23:30\nВс 10:00 - 23:30')


# @dp.message_handler(commands=['Расположение'])
async def place_pizza_command(message: types.message):
    await bott.send_message(message.from_user.id, 'Мы находимся по адресу:\n'
                                                  'г.Воронеж, пр. Революции, д. 20')


async def menu_pizza(message: types.message):
    await sqlite_db.sql_read(message)


async def close_key(message: types.message):
    await bott.send_message(message.from_user.id, 'Клавиатура убрана.'
                                                  '\nДля того, чтобы вернуть её, '
                                                  'введите "/start"', reply_markup=ReplyKeyboardRemove())


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help', ])
    dp.register_message_handler(time_work_command, commands=['Режим_работы'])
    dp.register_callback_query_handler(keys, lambda x: x.data)
    dp.register_callback_query_handler(offer.keys2, lambda x: x.data)
    # dp.register_callback_query_handler(back_to_menu, lambda query: query.data)
    dp.register_message_handler(place_pizza_command, commands=['Расположение'])
    dp.register_message_handler(menu_pizza, commands=['Меню_пиццерии'])
    dp.register_message_handler(close_key, commands=['Убрать_клавиатуру'])
