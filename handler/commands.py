import time
import random

from aiogram import Bot
from BD import del_user
from keyboards.inline import reply_kyq
from pyexpat.errors import messages
from keyboards.inline import reply_kyw
from keyboards.inline import reply_ky
from keyboards.inline import reply_key
from enum import global_enum
from mailbox import Message
from turtledemo.penrose import start
from aiogram import Router, types
from aiogram.filters import Command
from aiogram import F
from aiogram.types import FSInputFile
from aiogram.types import ReplyKeyboardRemove
from keyboards.inline import reply_kb
from handler.callback import callbacks_router
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State , StatesGroup
#from BD import logger
#from BD import get_note_by_id
from BD import cursor
from BD import load_user, save_user

command_router = Router()
fsm_router = Router()

fishing_bait = {2 : 50, 3 : 200 , 4 : 600 , 5 : 800}
fishing_rod = {2 : 100 , 3 : 300 , 4 : 500 , 5 : 1000}
listok = ['килька', 'плотва', 'карась']
cena = {"килька": 1, "плотва" : 3, "карась" : 5, "щука" : 7, "сом" : 10, 'семга' : 15 ,"тунец" : 20 }
money = 0
lvl_fishing_rod = 1
lvl_fishing_bait = 1

user_data = {}

def get_user_data(user_id):
    if user_id not in user_data:
        data = load_user(user_id)
        if data:
            money, lvl_rod, lvl_bait = data
        else:
            money, lvl_rod, lvl_bait = 0, 1, 1
            save_user(user_id, money, lvl_rod, lvl_bait)
        user_data[user_id] = {'money': money, 'lvl_rod': lvl_rod, 'lvl_bait': lvl_bait}
    return user_data[user_id]

def update_user_data(user_id):
    data = user_data[user_id]
    save_user(user_id, data['money'], data['lvl_rod'], data['lvl_bait'])

@command_router.message(Command("start"))
async def start(message:  types.Message):
    user_id = message.from_user.id
    get_user_data(user_id)
    await message.answer("Привет, я бот в котором ты сможешь побыть рыбаком! \nОбнови удочки что бы уменьшить шанс срывания рыбы с крючка\nОбнови приманки что бы разблокировать новые рыбы")
    await message.answer("Выбирайте:", reply_markup=reply_kb)

@command_router.message(F.text == "Закинуть удочку")
async def fishing(message:  types.Message):
    user_id = message.from_user.id
    data = get_user_data(user_id)
    a = (random.choice(listok))
    chance = random.randint(0, 100)
    a1 = cena[a]
    await message.answer("Процесс...", reply_markup=ReplyKeyboardRemove())
    time.sleep(3)
    lvl_fishing_rod = data['lvl_rod']
    if lvl_fishing_rod == 1:
        if chance < 40:
            data['money'] += a1
            update_user_data(user_id)
            await message.answer(f"Ты поймал рыбу {a}, за нее ты получишь - {a1} монет . Твой баланс - {data['money']} ", reply_markup=reply_kb)
            await message.answer(f"😊")
        else:
            await message.answer(f"Рыба сорвалась... хочешь еще? ", reply_markup=reply_kb)
            await message.answer(f"😭")
    if lvl_fishing_rod == 2:
        if chance < 50:
            data['money'] += a1
            update_user_data(user_id)
            await message.answer(f"Ты поймал рыбу {a}, за нее ты получишь - {a1} монет . Твой баланс - {data['money']} ", reply_markup=reply_kb)
            await message.answer(f"😊")
        else:
            await message.answer(f"Рыба сорвалась... хочешь еще? ", reply_markup=reply_kb)
            await message.answer(f"😭")
    if lvl_fishing_rod == 3:
        if chance < 60:
            data['money'] += a1
            update_user_data(user_id)
            await message.answer(f"Ты поймал рыбу {a}, за нее ты получишь - {a1} монет . Твой баланс - {data['money']} ", reply_markup=reply_kb)
            await message.answer(f"😊")
        else:
            await message.answer(f"Рыба сорвалась... хочешь еще? ", reply_markup=reply_kb)
            await message.answer(f"😭")
    if lvl_fishing_rod == 4:
        if chance < 70:
            data['money'] += a1
            update_user_data(user_id)
            await message.answer(f"Ты поймал рыбу {a}, за нее ты получишь - {a1} монет . Твой баланс - {data['money']} ", reply_markup=reply_kb)
            await message.answer(f"😊")
        else:
            await message.answer(f"Рыба сорвалась... хочешь еще? ", reply_markup=reply_kb)
            await message.answer(f"😭")
    if lvl_fishing_rod == 5:
        if chance < 90:
            data['money'] += a1
            update_user_data(user_id)
            await message.answer(f"Ты поймал рыбу {a}, за нее ты получишь - {a1} монет . Твой баланс - {data['money']} ", reply_markup=reply_kb)
            await message.answer(f"😊")
        else:
            await message.answer(f"Рыба сорвалась... хочешь еще? ", reply_markup=reply_kb)
            await message.answer(f"😭")

@command_router.message(F.text == "Удочку")
async def up_rod(message:  types.Message):
    user_id = message.from_user.id
    data = get_user_data(user_id)
    if data['lvl_rod'] == 1:
        if data['money'] > 100:
            data['lvl_rod'] = 2
            data['money'] -= 100
            update_user_data(user_id)
            await message.answer_photo(photo="https://sun9-13.userapi.com/impf/B-HOcl_DJB4IE2tt_0rKSGnBeBCdHXaJub3HJg/nc6_qAH7yho.jpg?size=514x426&quality=95&sign=4fc3644265a3135b5f1deaf0d7540c8c&c_uniq_tag=yLz387hX7gw67aL-EYizrZj2t8bpY2OFRwuEbLcroeM&type=album", caption = "Вы обновили удочку")
        else:
            await message.answer(f"Не хватает монет")
    elif data['lvl_rod'] == 2:
        if data['money'] > 300:
            data['lvl_rod'] = 3
            data['money'] -= 300
            update_user_data(user_id)
            await message.answer_photo(photo="https://sun9-13.userapi.com/impf/B-HOcl_DJB4IE2tt_0rKSGnBeBCdHXaJub3HJg/nc6_qAH7yho.jpg?size=514x426&quality=95&sign=4fc3644265a3135b5f1deaf0d7540c8c&c_uniq_tag=yLz387hX7gw67aL-EYizrZj2t8bpY2OFRwuEbLcroeM&type=album", caption = "Вы обновили удочку")
        elif data['money'] < 300:
            await message.answer(f"Не хватает монет")
    elif data['lvl_rod'] == 3:
        if data['money'] > 500:
            data['lvl_rod'] = 4
            data['money'] -= 500
            update_user_data(user_id)
            await message.answer_photo(photo="https://sun9-13.userapi.com/impf/B-HOcl_DJB4IE2tt_0rKSGnBeBCdHXaJub3HJg/nc6_qAH7yho.jpg?size=514x426&quality=95&sign=4fc3644265a3135b5f1deaf0d7540c8c&c_uniq_tag=yLz387hX7gw67aL-EYizrZj2t8bpY2OFRwuEbLcroeM&type=album", caption = "Вы обновили удочку")
        elif data['money'] < 500:
            await message.answer(f"Не хватает монет")
    elif data['lvl_rod'] == 4:
        if data['money'] > 1000:
            data['lvl_rod'] = 5
            data['money'] -= 1000
            update_user_data(user_id)
            await message.answer_photo(photo="https://sun9-13.userapi.com/impf/B-HOcl_DJB4IE2tt_0rKSGnBeBCdHXaJub3HJg/nc6_qAH7yho.jpg?size=514x426&quality=95&sign=4fc3644265a3135b5f1deaf0d7540c8c&c_uniq_tag=yLz387hX7gw67aL-EYizrZj2t8bpY2OFRwuEbLcroeM&type=album", caption = "Вы обновили удочку")
        elif data['money'] < 1000:
            await message.answer(f"Не хватает монет")

@command_router.message(F.text == "Приманку")
async def up_bait(message:  types.Message):
    user_id = message.from_user.id
    data = get_user_data(user_id)
    if data['lvl_bait'] == 1:
        if data['money'] > 50:
            data['lvl_bait'] = 2
            data['money'] -= 50
            update_user_data(user_id)
            listok.pop(0)
            listok.append("щука")
            await message.answer_photo(photo="https://sun9-13.userapi.com/impf/B-HOcl_DJB4IE2tt_0rKSGnBeBCdHXaJub3HJg/nc6_qAH7yho.jpg?size=514x426&quality=95&sign=4fc3644265a3135b5f1deaf0d7540c8c&c_uniq_tag=yLz387hX7gw67aL-EYizrZj2t8bpY2OFRwuEbLcroeM&type=album", caption = "Вы обновили приманку")
        elif data['money'] < 50:
            await message.answer(f"Не хватает монет")
    elif data['lvl_bait'] == 2:
        if data['money'] > 200:
            data['lvl_bait'] = 3
            data['money'] -= 200
            update_user_data(user_id)
            listok.pop(0)
            listok.append("сом")
            await message.answer_photo(photo="https://sun9-13.userapi.com/impf/B-HOcl_DJB4IE2tt_0rKSGnBeBCdHXaJub3HJg/nc6_qAH7yho.jpg?size=514x426&quality=95&sign=4fc3644265a3135b5f1deaf0d7540c8c&c_uniq_tag=yLz387hX7gw67aL-EYizrZj2t8bpY2OFRwuEbLcroeM&type=album", caption = "Вы обновили приманку")
        elif data['money'] < 200:
            await message.answer(f"Не хватает монет")
    elif data['lvl_bait'] == 3:
        if data['money'] > 600:
            data['lvl_bait'] = 4
            data['money'] -= 600
            update_user_data(user_id)
            listok.pop(0)
            listok.append("семга")
            await message.answer_photo(photo="https://sun9-13.userapi.com/impf/B-HOcl_DJB4IE2tt_0rKSGnBeBCdHXaJub3HJg/nc6_qAH7yho.jpg?size=514x426&quality=95&sign=4fc3644265a3135b5f1deaf0d7540c8c&c_uniq_tag=yLz387hX7gw67aL-EYizrZj2t8bpY2OFRwuEbLcroeM&type=album", caption = "Вы обновили приманку")
        elif data['money'] < 600:
            await message.answer(f"Не хватает монет")
    elif data['lvl_bait'] == 4:
        if data['money'] > 800:
            data['lvl_bait'] = 5
            data['money'] -= 800
            update_user_data(user_id)
            listok.pop(0)
            listok.append("тунец")
            await message.answer_photo(photo="https://sun9-13.userapi.com/impf/B-HOcl_DJB4IE2tt_0rKSGnBeBCdHXaJub3HJg/nc6_qAH7yho.jpg?size=514x426&quality=95&sign=4fc3644265a3135b5f1deaf0d7540c8c&c_uniq_tag=yLz387hX7gw67aL-EYizrZj2t8bpY2OFRwuEbLcroeM&type=album", caption = "Вы обновили приманку")
        elif data['money'] < 800:
            await message.answer(f"Не хватает монет")

@command_router.message(F.text == "Профиль")
async def profile(message:  types.Message):
    user_id = message.from_user.id
    data = get_user_data(user_id)
    await message.answer(f"кол-во монет - {data['money']}, уровень удочки - {data['lvl_rod']}, уровень приманки - {data['lvl_bait']}")

@command_router.message(F.text == "Цены")
async def ceni(message:  types.Message):
    await message.answer(f"Удочки или приманки?",reply_markup=reply_key)

@command_router.message(F.text == "Удочки")
async def rods(message:  types.Message):
    await message.answer(f"Удочка 2 уровня стоит {fishing_rod[2]} \nУдочка 3 уровня стоит {fishing_rod[3]} \nУдочка 4 уровня стоит {fishing_rod[4]} \nУдочка 5 уровня стоит {fishing_rod[5]}",reply_markup=reply_kb)

@command_router.message(F.text == "Приманки")
async def baits(message:  types.Message):
    await message.answer(f"Приманка 2 уровня стоит {fishing_bait[2]} \nПриманка 3 уровня стоит {fishing_bait[3]} \nПриманка 4 уровня стоит {fishing_bait[4]} \nПриманка 5 уровня стоит {fishing_rod[5]}",reply_markup=reply_kb)

@command_router.message(F.text == "Назад")
async def back(message:  types.Message):
    await message.answer(text = "Вы вернулись в главное меню", reply_markup=reply_kb)

@command_router.message(F.text == "Магазин")
async def rod_bait(message:  types.Message):
    await message.answer(text = "Купить или Посмотреть цены?", reply_markup=reply_kyw)

@command_router.message(F.text == "Купить")
async def buy(message:  types.Message):
    await message.answer(text = "Выбирайте что купить", reply_markup=reply_ky)

@command_router.message(F.text == "Сбросить прогресс")
async def profile(message:  types.Message):
    await message.answer(text = "Точно? Вы потеряете весь прогресс", reply_markup=reply_kyq)

@command_router.message(F.text == "Точно")
async def profile(message:  types.Message):
    del_user(message.from_user.id)
    money = 0
    lvl_fishing_rod = 0
    lvl_fishing_bait = 0
    await message.answer(text = "Вы сбросили прогресс", reply_markup=reply_kb)



