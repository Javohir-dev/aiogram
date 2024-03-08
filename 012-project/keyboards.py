from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton,
)

btn = ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = KeyboardButton(text="/help")
btn2 = KeyboardButton(text="/info")
btn3 = KeyboardButton(text="Random photo")
btn.add(btn1, btn2).add(btn3)

# Inline_btn = InlineKeyboardMarkup(row_width=2)
# inline_1 = InlineKeyboardButton(text="❤️", callback_data="like")
# inline_2 = InlineKeyboardButton(text="👎", callback_data="dislike")
# Inline_btn.add(inline_1, inline_2)
