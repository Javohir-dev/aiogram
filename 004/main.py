from config import API_TOKEN
import string
import random

from aiogram import Dispatcher, Bot, executor, types

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)


INFO = "Bu bot sizga hariflarni tasodify tarzda tanlab beradi.\n\nHarfni olish uchun /letter ga bosing"
START_COMMAND = "<b>👋 Assalomu alaykum,\n</b>Botimisga hush kelibsiz."
HELP_COMMAND = """
/help - barcha buyruqlar.
/start - Jarayonni boshlash.
/info - Bot haqida ma'lumot.
 - 
/count - Shunchaki sanash uchun.
"""
count = 0


async def on_startup(_):
    print("Bot started successfuly.\nYou can go to the bot and use it.\nOK")


@dp.message_handler(commands=["help"])
async def help(message: types.Message):
    await message.reply(HELP_COMMAND)


@dp.message_handler(commands=["start", "restart"])
async def welcome(message: types.Message):
    await message.answer(START_COMMAND, parse_mode="HTML")
    await message.delete()


@dp.message_handler(commands=["give"])
async def welcome(message: types.Message):
    await bot.send_sticker(
        message.from_user.id,
        sticker="CAACAgIAAxkBAAELl0Fl4poCIbsm1Wpa19xujD7-pjKGjgACJAAD8_KOP3RlX-q5ZjUqNAQ",
    )
    await message.delete()


@dp.message_handler()
async def send_emoji(message: types.Message):
    await message.reply(message.text.title() + " 🔥")


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)
