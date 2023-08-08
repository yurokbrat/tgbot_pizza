from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Оформить_новый_заказ')
b2 = KeyboardButton('/Узнать_статус_заказа')
b3 = KeyboardButton('/Отменить_заказ')
b4 = KeyboardButton('/Убрать_клавиатуру')
b5 = KeyboardButton('/Назад')
kb_client_offer = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_offer.add(b1).add(b2).add(b3).row(b4,b5)