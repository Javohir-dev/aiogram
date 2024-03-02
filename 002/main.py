from config import API_TOKEN

from aiogram import Dispatcher, Bot, executor, types

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)

START_COMMAND = "👋 Assalomu alaykum,\nBotimisga hush kelibsiz."
HELP_COMMAND = """
/help - barcha buyruqlar.
/start - Jarayonni boshlash.
"""


@dp.message_handler(commands=["help"])
async def help(message: types.Message):
    await message.reply(HELP_COMMAND)


@dp.message_handler(commands=["start", "restart"])
async def welcome(message: types.Message):
    await message.answer(START_COMMAND)
    await message.delete()


# @dp.message_handler(commands=["help"])
# async def welcome(message: types.Message):
#     await message.reply(HELP_COMMAND)


if __name__ == "__main__":
    print("Bot started successfuly...")
    executor.start_polling(dp)
