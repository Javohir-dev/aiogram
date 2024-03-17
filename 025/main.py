from aiogram import Dispatcher, Bot, executor, types
from aiogram.utils.callback_data import CallbackData
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    InlineQueryResultArticle,
    InputTextMessageContent,
)

from config import API_TOKEN
import hashlib

cd = CallbackData("ikb", "action")  # pattern
bot = Bot(API_TOKEN)
dp = Dispatcher(bot)


def get_ikb() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("Button 1", callback_data=cd.new("push_1"))],
            [InlineKeyboardButton("Button 2", callback_data=cd.new("push_2"))],
        ]
    )

    return ikb


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message) -> None:
    await message.answer(
        text="Welcome to my YouTubeBot! Don't forgot subscribe my YouTube channale.",
        reply_markup=get_ikb(),
    )
    await message.delete()


@dp.callback_query_handler(cd.filter(action="push_1"))
async def cd_push_one(callback: types.CallbackQuery) -> None:
    await callback.answer("Hello")


@dp.callback_query_handler(cd.filter(action="push_2"))
async def cd_push_two(callback: types.CallbackQuery) -> None:
    await callback.answer("World!")


@dp.inline_handler()
async def inline_echo(inline_query: types.InlineQuery) -> None:
    text = inline_query.query or "Echo"
    input_content = InputTextMessageContent(text)
    result_id: str = hashlib.md5(text.encode()).hexdigest()  # Create unique id

    item = InlineQueryResultArticle(
        input_message_content=input_content,
        id=result_id,
        title="Yuborish uchun bosing",
    )
    await bot.answer_inline_query(
        inline_query_id=inline_query.id, results=[item], cache_time=1
    )


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True)
