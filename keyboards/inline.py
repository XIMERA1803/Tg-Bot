from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
reply_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text ='закинуть удочку', callback = "fishing")],
        [KeyboardButton(text ="Обновить", callback = "bait")],
        [KeyboardButton(text = 'цены',callback = "celi")],
        [KeyboardButton(text ="профиль", callback = "profil")]

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
























