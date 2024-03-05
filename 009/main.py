from config import API_TOKEN

from aiogram import Dispatcher, Bot, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)

ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text="Button 1", url="https://www.youtube.com/@JavohirWeb")
ib2 = InlineKeyboardButton(text="Button 2", url="https://www.youtube.com/@JavohirWeb")
# ikb.add(ib1).add(ib2)  # Alohida qotorga qo'yasi
ikb.add(ib1, ib2)  # Bitta qotorga qo'yadi.

INFO = "Bu bot sizga hariflarni tasodify tarzda tanlab beradi.\n\nHarfni olish uchun /letter ga bosing"
START_COMMAND = "<b>👋 Assalomu alaykum,\n</b>Botimisga hush kelibsiz."
HELP_COMMAND = """
<b>🆘 Yordam | Bu yerda barcha buyruqlarni ko'rishingiz mumkin.</b>

<b>🔹 Asosiy buyruqlar</b>
<b>/help</b> - <em>barcha buyruqlar.</em>
<b>/start</b> - <em>Jarayonni boshlash.</em>


<b>🔥 @ch_wikibot 🔥</b>
"""


@dp.message_handler(commands=["start", "restart"])
async def welcome(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text="Hello world!",
        parse_mode="HTML",
        reply_markup=ikb,
    )


@dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text=HELP_COMMAND,
        parse_mode="HTML",
        # reply_markup=ReplyKeyboardRemove(),  # /help bosilgandan keyin keyboard yoqoladi
    )


# @dp.message_handler(commands=["image"])
# async def send_image(message: types.Message):
#     await bot.send_photo(
#         chat_id=message.chat.id,
#         photo="https://eurotuner.de/wp-content/uploads/2020/08/Porsche-992-Turbo-S-Sportfedern-Heck-1024x683.jpg",
#     )


# @dp.message_handler()
# async def send_cat(message: types.Message):
#     if message.text == "❤️":
#         return await bot.send_sticker(
#             chat_id=message.from_user.id,
#             sticker="CAACAgQAAxkBAAELl0Nl4pzw-g_eMshFQQPhVWf7PvozzAAC6AkAAm0F6VN39FXEdCyjuDQE",
#         )
#     await message.answer("I don't understand.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
