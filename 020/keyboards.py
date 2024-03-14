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

btn_photo = ReplyKeyboardMarkup(resize_keyboard=True)
random1 = KeyboardButton(text="🖼 Random")
random2 = KeyboardButton(text="⬅️ Bekor qilish")
btn_photo.add(random1, random2)
Inline_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=f"❤️", callback_data="like"),
            InlineKeyboardButton(text="👎", callback_data="dislike"),
        ],
        [
            InlineKeyboardButton(text="Close", callback_data="close"),
            InlineKeyboardButton(text="wrong", callback_data="knjnbjkjh"),
        ],
    ]
)
