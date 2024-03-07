from config import API_TOKEN

from aiogram import Dispatcher, Bot, executor, types
from keyboards import Inline_btn, btn

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)

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
        text="Asosiy sahifaga hush kerlibsiz.",
        parse_mode="HTML",
        reply_markup=btn,
    )


@dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text=HELP_COMMAND,
        parse_mode="HTML",
        # reply_markup=ReplyKeyboardRemove(),  # /help bosilgandan keyin keyboard yoqoladi
    )


@dp.message_handler(commands=["vote"])
async def vote_command(message: types.Message):
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo="https://avatars.mds.yandex.net/i?id=d405f07db07abd5c021ba96300436a8d4576a2b1-10385057-images-thumbs&n=13",
        caption="Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
        reply_markup=Inline_btn,
    )


@dp.callback_query_handler()
async def vote_callback(callback: types.CallbackQuery):
    if callback.data == "like":
        return await callback.answer(text="Sizga bu rasm yoqqanidan hursandmiz ) ")
    await callback.answer(text="Holatni yaxshilash ustida ish olib boramiz!")


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True)
