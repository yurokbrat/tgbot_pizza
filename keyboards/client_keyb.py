from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Режим_работы')
b2 = KeyboardButton('/Расположение')
b3 = KeyboardButton('/Меню_пиццерии')
b4 = KeyboardButton('/Заказы')
b5 = KeyboardButton('/Убрать_клавиатуру')
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(b1).add(b2).row(b3, b4).add(b5)
