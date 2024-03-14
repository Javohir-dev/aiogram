from aiogram import Dispatcher, Bot, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove

from config import API_TOKEN

from keyboards import Inline_btn

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)

is_voted = False


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message) -> None:
    await bot.send_photo(
        chat_id=message.chat.id,
        photo="https://a.d-cd.net/85d68d5s-1920.jpg",
        caption="Do you like it?",
        reply_markup=Inline_btn,
    )
    await message.delete()


@dp.callback_query_handler(text="close")
async def ikb_close_cb(callback: types.CallbackQuery) -> None:
    await callback.message.delete()


@dp.callback_query_handler(text="like")
async def ikb_close_cb(callback: types.CallbackQuery) -> None:
    global is_voted
    if not is_voted:
        is_voted = True
        await callback.answer("❤ Liked")
    else:
        await callback.answer(show_alert=True, text="⚠ You have already voted!")


@dp.callback_query_handler(text="dislike")
async def ikb_close_cb(callback: types.CallbackQuery) -> None:
    global is_voted
    if not is_voted:
        is_voted = True
        await callback.answer("👎 disliked")
    else:
        await callback.answer(show_alert=True, text="⚠ You have already voted!")


@dp.callback_query_handler()
async def ikb_close_cb(callback: types.CallbackQuery) -> None:
    await callback.answer(show_alert=True, text="⚠Something is wrong!")


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True)
