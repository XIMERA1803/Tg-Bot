from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
reply_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text ='закинуть удочку', callback = "fishing")],
        [KeyboardButton(text = 'обновить удочку',callback = "money")]

    ],
    resize_keyboard=True
)
























