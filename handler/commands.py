import time
import random
from mailbox import Message
from turtledemo.penrose import start
from aiogram import Router, types
from aiogram.filters import Command
from aiogram import F
import aiogram
from aiogram.types import FSInputFile
from aiogram.types import ReplyKeyboardRemove
from keyboards.inline import reply_kb
from handler.callback import callbacks_router


command_router = Router()
fishing_rod = {2 : 100 , 3 : 300 , 4 : 500 , 5 : 1000}
listok = ['килька', 'плотва', 'карась', 'щука', 'сом']
cena = {"килька": 1, "плотва" : 3, "карась" : 5, "щука" : 7, "сом" : 10}
money = 0
lvl_fishing_rod = 1
@command_router.message(Command("start"))
async def start(message:  types.Message):
    await message.answer("привет, я бот в котором ты сможешь побыть рыбаком!")
    await message.answer("выбирайте:", reply_markup=reply_kb)
@command_router.message(F.text == "закинуть удочку")
async def fishing(message:  types.Message):
    a = (random.choice(listok))
    chance = random.randint(0, 100)
    a1 = cena[a]
    global money
    money = money + a1
    await message.answer("процесс...")
    time.sleep(3)
    if lvl_fishing_rod == 1:
        if chance > 30 :
            await message.answer(f"рыба сорвалась... хочешь еще? жми на кнопку ./start")
        else:
            await message.answer(f"ты поймал рыбу {a}, за нее ты получишь - {a1} монет . Твой баланс - {money}")
    """if lvl_fishing_rod == 2:
        if chance > 40:
            await message.answer(f"рыба сорвалась... хочешь еще? жми /start")
        else:
            await message.answer(f"ты поймал рыбу {a}, за нее ты получишь - {a1} монет . Твой баланс - {money}")
    if lvl_fishing_rod == 3:
        if chance < 50:
            await message.answer(f"рыба сорвалась... хочешь еще? жми /start")
        else:
            await message.answer(f"ты поймал рыбу {a}, за нее ты получишь - {a1} монет . Твой баланс - {money}")
    if lvl_fishing_rod == 4:
        if chance < 60:
            await message.answer(f"рыба сорвалась... хочешь еще? жми /start")
        else:
            await message.answer(f"ты поймал рыбу {a}, за нее ты получишь - {a1} монет . Твой баланс - {money}")
    if lvl_fishing_rod == 5:
        if chance < 70:
            await message.answer(f"рыба сорвалась... хочешь еще? жми /start")
        else:
            await message.answer(f"ты поймал рыбу {a}, за нее ты получишь - {a1} монет . Твой баланс - {money}")"""
"""@command_router.message(F.text == "обновить удочку")
async def fishing(message:  types.Message):
    if lvl_fishing_rod == 1:
        if money < fishing_rod[1]:
            await message.answer(f"")"""