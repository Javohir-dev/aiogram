from aiogram import Dispatcher, Bot, executor, types
from aiogram.dispatcher.filters import Text

from config import API_TOKEN
from keyboards import btn, btn_photo
import random

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)

HELP_TEXT = """
<b>All commands:</b>
/start - Boshlash
/help - Barcha buyruqlar
/info - BOT haqida barchasi

<a href="https://t.me/ch_wikibot">AiogramBot 🔥</a>
"""

INFO_TEXT = """
<b>All information:</b>

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.
"""

photo_list = [
    "https://avatars.mds.yandex.net/i?id=f1e3b2717160b57cf3a389d6ad25f73a718a6cbb-4841251-images-thumbs&n=13",
    "https://w.forfun.com/fetch/49/4981dd7cd0617568014d75b5c7f21e2a.jpeg",
    "https://mobimg.b-cdn.net/v3/fetch/70/703e3aefd9500eff0f63294bc383ac2a.jpeg",
    "https://wallpapers.com/images/hd/cabins-in-the-forest-t4bsw0bhu7uaa7yh.jpg",
]


@dp.message_handler(Text(equals="Random photo"))
async def open_kb_photo(message: types.Message):
    await message.answer(
        text="Turlixil rasimlarni olish uchun 'Random' tugmasiga bosing.",
        reply_markup=btn_photo,
    )


@dp.message_handler(Text(equals="⬅️ Bekor qilish"))
async def main_page(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text="Asosiy sahifaga.",
        reply_markup=btn,
    )


@dp.message_handler(Text(equals="🖼 Random"))
async def rand_photo(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo=random.choice(photo_list))


@dp.message_handler(commands=["start", "restart"])
async def welcome(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text="Asosiy sahifaga hush kerlibsiz.",
        parse_mode="HTML",
        reply_markup=btn,
    )
    await bot.send_sticker(
        message.chat.id,
        sticker="CAACAgIAAxkBAAELoNRl6V0r8iSscT7hNs0UW01LcaYtTQACAQEAAladvQoivp8OuMLmNDQE",
    )


@dp.message_handler(commands=["help"])
async def cmd_help(message: types.Message):
    await message.answer(
        text=HELP_TEXT,
        parse_mode="HTML",
        reply_markup=btn,
    )
    await message.delete()


@dp.message_handler(commands=["info"])
async def cmd_info(message: types.Message):
    await message.answer(
        text=INFO_TEXT,
        parse_mode="HTML",
        reply_markup=btn,
    )


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True)
