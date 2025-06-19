from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
reply_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text ='закинуть удочку', callback = "fishing")],
        [KeyboardButton(text ="обновить приманку", callback = "bait")],
        [KeyboardButton(text = 'обновить удочку',callback = "money")],
        [KeyboardButton(text = 'цены',callback = "celi")],
        [KeyboardButton(text ="профиль", callback = "profil")]

    ],
    resize_keyboard=True
)
reply_key = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text ='Удочки', callback = "fishing")],
        [KeyboardButton(text ='Назад', callback = "fishing")],
        [KeyboardButton(text ='Приманки', callback = "в")]
    ],
    resize_keyboard=True
)
























