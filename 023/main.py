from aiogram import Dispatcher, Bot, executor, types
from aiogram.utils.callback_data import CallbackData
from aiogram.dispatcher.filters import Text
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from config import API_TOKEN

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)
cd = CallbackData("ikb", "action")

ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("Button", callback_data=cd.new("push"))],
    ]
)


# @dp.callback_query_handler(lambda callback_query: callback_query.data == "hello")
# async def ikb_callback(callback: types.CallbackQuery) -> None:
#     await callback.answer("🔥❤️ Something...")


@dp.callback_query_handler(cd.filter())
async def ikb_callback(callback: types.CallbackQuery, callback_data: dict) -> None:
    print(callback_data)
    if callback_data["action"] == "push":
        await callback.answer("🔥❤️ Something...")


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Nothing...", reply_markup=ikb)
    await message.delete()


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True)
