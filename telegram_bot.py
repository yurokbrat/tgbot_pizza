from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db, devilery_db
from handlers import client, other, admin, offer


async def on_startup(_):
    print('Бот вышел в онлайн')
    sqlite_db.sql_menu_start()


client.register_handlers_client(dp)
offer.register_handlers_client_offer(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
