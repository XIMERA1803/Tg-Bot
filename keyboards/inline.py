from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
reply_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text ='Закинуть удочку', callback = "fishing")],
        [KeyboardButton(text ="Магазин", callback = "bait")],
        [KeyboardButton(text ="Профиль", callback = "profil")],
        [KeyboardButton(text ="Сбросить прогресс", callback = "bait")]

    ],
    resize_keyboard=True
)
reply_key = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text ='Удочки', callback = "fishing")],
        [KeyboardButton(text ='Приманки', callback = "в")],
        [KeyboardButton(text ='Назад', callback = "fishing")]

    ],
    resize_keyboard=True
)


reply_ky = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text ='Удочку', callback = "fishing")],
        [KeyboardButton(text ='Приманку', callback = "в")],
        [KeyboardButton(text ='Назад', callback = "fishing")]
    ],
    resize_keyboard=True
)

reply_kyw = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text ='Цены', callback = "fishing")],
        [KeyboardButton(text ='Купить', callback = "fishing")],
        [KeyboardButton(text ='Назад', callback = "fishing")]
    ],
    resize_keyboard=True
)


reply_kyq = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text ='Точно', callback = "fishing")],
    ],
    resize_keyboard=True
)


















