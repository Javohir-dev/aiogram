from aiogram import Dispatcher, Bot, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import (
    ReplyKeyboardRemove,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from config import API_TOKEN

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)

num: int = 0


def get_inline_kb() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("Increase", callback_data="btn_increase"),
                InlineKeyboardButton("Decrease", callback_data="btn_decrease"),
            ],
        ]
    )
    return ikb


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message) -> None:
    await message.answer(f"The corrent number is {num}", reply_markup=get_inline_kb())


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith("btn"))
async def callback_ikb(callback: types.CallbackQuery) -> None:
    global num
    if callback.data == "btn_increase":
        num += 1
        await callback.message.edit_text(
            f"The corrent number is {num}", reply_markup=get_inline_kb()
        )
    elif callback.data == "btn_decrease":
        if num > 0:
            num -= 1
            await callback.message.edit_text(
                f"The corrent number is {num}", reply_markup=get_inline_kb()
            )
        else:
            await callback.answer(show_alert=True, text="⚠ Something is wrong!")


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True)
