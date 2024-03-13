from aiogram import Dispatcher, Bot, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove

from config import API_TOKEN
from keyboards import Inline_btn, btn, btn_photo
import random
from pprint import pprint

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

photos = dict(
    zip(
        photo_list,
        [
            "Bu yerda sizning reklamangiz bo'lishi mumkin edi.",
            "Bu yerda sizning reklamangiz bo'lishi mumkin edi.",
            "Bu yerda sizning reklamangiz bo'lishi mumkin edi.",
            "Bu yerda sizning reklamangiz bo'lishi mumkin edi.",
        ],
    )
)
random_photo = random.choice(list(photos.keys()))
flag = False


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await bot.send_photo(
        chat_id=message.chat.id,
        photo="https://img.goodfon.ru/wallpaper/nbig/c/34/2022-porsche-911-gt3-r-porsche-911-gt3-r-sports-car.jpg",
        caption="Sizga rasim yoqqan bo'lsa ❤️ bosing",
        reply_markup=Inline_btn,
    )


@dp.callback_query_handler()
async def ikb_cb_handler(callback: types.CallbackQuery):
    print(callback)
    if callback.data == "like":
        await callback.answer("❤️Like uchun rahmat )")
    await callback.answer("Yaxshilashga harakat qilamiz.")


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True)
