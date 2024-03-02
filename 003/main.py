from config import API_TOKEN
import string
import random

from aiogram import Dispatcher, Bot, executor, types

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)


INFO = "Bu bot sizga hariflarni tasodify tarzda tanlab beradi.\n\nHarfni olish uchun /letter ga bosing"
START_COMMAND = "👋 Assalomu alaykum,\nBotimisga hush kelibsiz."
HELP_COMMAND = """
/help - barcha buyruqlar.
/start - Jarayonni boshlash.
/info - Bot haqida ma'lumot.
 - 
/count - Shunchaki sanash uchun.
"""
count = 0


@dp.message_handler(commands=["help"])
async def help(message: types.Message):
    await message.reply(HELP_COMMAND)


@dp.message_handler(commands=["start", "restart"])
async def welcome(message: types.Message):
    await message.answer(START_COMMAND)
    await message.delete()


@dp.message_handler(commands=["count"])
async def check_count(message: types.Message):
    global count
    await message.answer(f"Count: {count}")
    await message.delete()
    count += 1


@dp.message_handler()
async def check_zero(message: types.Message):
    global count
    if "0" in message.text:
        return await message.answer("Yes")
    await message.answer("No")


@dp.message_handler(commands=["info"])
async def desc_command(message: types.Message):
    await message.answer(INFO)
    await message.delete()


@dp.message_handler(commands=["letter"])  # ASCCII
async def send_random_letter(message: types.Message):
    await message.reply(random.choice(string.ascii_letters))


if __name__ == "__main__":
    print("Bot started successfuly...")
    executor.start_polling(dp)
