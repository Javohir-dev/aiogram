from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_keyboard() -> ReplyKeyboardMarkup:
    keyboard_button = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard_button.add(KeyboardButton("Ishni boshlash."))

    return keyboard_button


def get_cancel() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton("⬅️ Bekor qilish")
    )
