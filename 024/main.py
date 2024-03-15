from aiogram import Dispatcher, Bot, executor, types
from aiogram.utils.callback_data import CallbackData
from aiogram.utils.exceptions import BotBlocked
from aiogram.dispatcher.filters import Text
from aiogram.types import (
    ReplyKeyboardRemove,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from config import API_TOKEN
import asyncio

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message) -> None:
    await asyncio.sleep(10)
    await message.answer("Loading...")


@dp.errors_handler(exception=BotBlocked)
async def error_bot_blocked(update: types.Update, exception: BotBlocked) -> bool:
    print("Habar jo'nataolmaysiz, chunki biz blocklandik")
    return True


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True)
