import sqlite3 as sq

from aiogram.types import message

from create_bot import bott

def sql_orders_start():
    global base, cur
    base = sq.connect('orders.db')
    cur = base.cursor()
    if base:
        print('Data base delivery was connected')
    base.execute('CREATE TABLE IF NOT EXISTS order(id TEXT, number_order TEXT, phone TEXT, address TEXT, status TEXT)')
    base.commit()

async def sql_read_status_command(id):
    for ret in cur.execute('SELECT status FROM delivery WHERE id = ?', (id,)).fetchall():
        await bott.send_message(message.from_user.id, f'Заказ № {ret[0]}\nСтатус заказа: {ret[-1]}')
    base.commit()