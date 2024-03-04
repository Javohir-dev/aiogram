from config import API_TOKEN

from aiogram import Dispatcher, Bot, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)
kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)  #!
# kb = ReplyKeyboardMarkup(resize_keyboard=True)  #!
btn_help = KeyboardButton("/help")
btn_image = KeyboardButton("/image")
btn_location = KeyboardButton("/location")
# kb.add(btn_help).add(btn_image).add(btn_location)  #!
# kb.insert(btn_help).insert(btn_image).insert(btn_location)  #!
kb.add(btn_help).insert(btn_image).add(btn_location)  #!


INFO = "Bu bot sizga hariflarni tasodify tarzda tanlab beradi.\n\nHarfni olish uchun /letter ga bosing"
START_COMMAND = "<b>👋 Assalomu alaykum,\n</b>Botimisga hush kelibsiz."
HELP_COMMAND = """
<b>🆘 Yordam | Bu yerda barcha buyruqlarni ko'rishingiz mumkin.</b>

<b>🔹 Asosiy buyruqlar</b>
<b>/help</b> - <em>barcha buyruqlar.</em>
<b>/start</b> - <em>Jarayonni boshlash.</em>


<b>🔥 @ch_wikibot 🔥</b>
"""
count = 0


async def on_startup(_):
    print("Bot started successfuly.\nYou can go to the bot and use it.\nOK")


# @dp.message_handler(commands=["help"])
# async def help_command(message: types.Message):
#     await message.reply(HELP_COMMAND, parse_mode="HTML")


@dp.message_handler(commands=["start", "restart"])
async def welcome(message: types.Message):
    await message.answer(START_COMMAND, parse_mode="HTML", reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text=HELP_COMMAND,
        parse_mode="HTML",
        reply_markup=ReplyKeyboardRemove(),  # /help bosilgandan keyin keyboard yoqoladi
    )


@dp.message_handler(commands=["image"])
async def send_image(message: types.Message):
    await bot.send_photo(
        chat_id=message.chat.id,
        photo="https://eurotuner.de/wp-content/uploads/2020/08/Porsche-992-Turbo-S-Sportfedern-Heck-1024x683.jpg",
    )


@dp.message_handler(commands=["location"])
async def send_point(message: types.Message):
    await bot.send_location(
        chat_id=message.from_user.id,
        latitude=40.899867,
        longitude=69.318151,
    )
    await bot.send_location(
        chat_id=message.chat.id,
        latitude=40.899867,
        longitude=69.318151,
    )
    await message.delete()


@dp.message_handler()
async def send_message(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text=message)
    await message.delete()


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
