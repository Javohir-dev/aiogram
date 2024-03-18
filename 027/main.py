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

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)
user_data: str


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message) -> None:
    await message.answer(
        text="Welcome to my YouTubeBot! Don't forgot subscribe my YouTube channale.",
    )
    await message.delete()


@dp.message_handler()
async def text_handler(message: types.Message) -> None:
    global user_data
    user_data = message.text
    await message.answer(text="Your data is saved.")


@dp.inline_handler()
async def inline_echo(inline_query: types.InlineQuery) -> None:
    global user_data
    text = inline_query.query or "Echo"
    result_id: str = hashlib.md5(text.encode()).hexdigest()  # Create unique id
    input_content = InputTextMessageContent(
        f"<b>{text}</b> - {user_data}", parse_mode="HTML"
    )

    item = InlineQueryResultArticle(
        id=result_id,
        title=text,
        description="This is a description",
        input_message_content=input_content,
    )
    await bot.answer_inline_query(
        inline_query_id=inline_query.id, results=[item], cache_time=1
    )


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True)
