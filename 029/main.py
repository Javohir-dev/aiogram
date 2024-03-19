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
import uuid

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
    text = inline_query.query or "Empty 🧩"
    # result_id: str = hashlib.md5(text.encode()).hexdigest()  # Create unique id
    input_content_bold = InputTextMessageContent(f"*{text}*", parse_mode="markdown")
    input_content_italic = InputTextMessageContent(f"_{text}_", parse_mode="markdown")

    item_1 = InlineQueryResultArticle(
        id=str(uuid.uuid4()),
        input_message_content=input_content_bold,
        title="Bold",
        description=text,
        thumb_url="https://yt3.googleusercontent.com/ytc/APkrFKb0UXzvb1r-2QnSfVJ088H-L6uAiracg9Q_qVn6=s900-c-k-c0x00ffffff-no-rj",
    )
    item_2 = InlineQueryResultArticle(
        id=str(uuid.uuid4()),
        input_message_content=input_content_italic,
        title="Bold",
        description=text,
        thumb_url="https://images.squarespace-cdn.com/content/v1/5eab7bbcd799bb4c8b71ef8b/1595364445405-3OZLBBY92KSHPT54044Y/italic-BW.png?format=1500w",
    )
    await bot.answer_inline_query(
        inline_query_id=inline_query.id, results=[item_1, item_2], cache_time=0.5
    )


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True)
