from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton,
)

btn = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
btn1 = KeyboardButton(text="/links")
btn.add(btn1)

ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text="YouTube", url="https://www.youtube.com/@JavohirWeb")
ib2 = InlineKeyboardButton(text="Challenge", url="https://t.me/challengeman_tm")
# ikb.add(ib1).add(ib2)  # Alohida qotorga qo'yasi
ikb.add(ib1, ib2)  # Bitta qotorga qo'yadi.
