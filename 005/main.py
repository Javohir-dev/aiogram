from config import API_TOKEN
import string
import random

from aiogram import Dispatcher, Bot, executor, types

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)


INFO = "Bu bot sizga hariflarni tasodify tarzda tanlab beradi.\n\nHarfni olish uchun /letter ga bosing"
START_COMMAND = "<b>👋 Assalomu alaykum,\n</b>Botimisga hush kelibsiz."
HELP_COMMAND = """
<b>🆘 Yordam | Bu yerda barcha buyruqlarni ko'rishingiz mumkin.</b>

<b>🔹 Asosiy buyruqlar</b>
<b>/help</b> - <em>barcha buyruqlar.</em>
<b>/start</b> - <em>Jarayonni boshlash.</em>
<b>/info</b> - <em>Bot haqida ma'lumot.</em>

<b>🔸 Yordamchi buyruqlar</b>
<b>/count</b> - <em>Shunchaki sanash uchun.</em>
<b>/give</b> - <em>give olish uchun.</em>
<b>/emoji</b> - <em>Emoji olish uchun.</em>


<b>🔥 @ch_wikibot 🔥</b>
"""
count = 0


async def on_startup(_):
    print("Bot started successfuly.\nYou can go to the bot and use it.\nOK")


@dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
    await message.reply(HELP_COMMAND, parse_mode="HTML")


@dp.message_handler(commands=["start", "restart"])
async def welcome(message: types.Message):
    await message.answer(START_COMMAND, parse_mode="HTML")
    await message.delete()


@dp.message_handler(commands=["give"])
async def send_give(message: types.Message):
    await bot.send_sticker(
        message.from_user.id,
        sticker="CAACAgQAAxkBAAELl0Vl4p3J4ksD-vYThSfRctCBYfB1dAACIh0AAlF9AAFQbzZh3VBYo6U0BA",
    )
    await message.delete()


@dp.message_handler(commands=["emoji"])
async def send_emoji(message: types.Message):
    await message.reply("Qarang qanday yoqimtoy mushik" + " 💖")
    await bot.send_sticker(
        message.from_user.id,
        sticker="CAACAgQAAxkBAAELl0Nl4pzw-g_eMshFQQPhVWf7PvozzAAC6AkAAm0F6VN39FXEdCyjuDQE",
    )


@dp.message_handler(content_types=["sticker"])
async def send_sticker_id(message: types.Message):
    await message.answer(
        f"✅ <b>Sticker id:</b> <code>{message.sticker.file_id}</code>",
        parse_mode="HTML",
    )


@dp.message_handler()
async def count(message: types.Message):
    """User jo'natgan message ichida nechta ✅ borligini sanab qaytaradi."""
    await message.answer(text=str(message.text.count("✅")))


@dp.message_handler()
async def send_emoji(message: types.Message):
    if message.text == "❤️":
        await message.reply("🖤")
    elif message.text == "🖤":
        await message.reply("❤️")


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)
