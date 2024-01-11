from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

location_keys = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🏦 Eng yaqin bankni topish", callback_data="mylocation")
        ]
    ])