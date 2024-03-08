from aiogram import Dispatcher, Bot, executor, types

from config import API_TOKEN
from keyboards import btn

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


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer(
        "Assalomu alaykum, Botimizga hush kelibsiz.",
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
