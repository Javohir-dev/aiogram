from aiogram import Dispatcher, Bot, executor, types
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage


from config import API_TOKEN

# from sqlite import start_db, create_profile, edit_profile

# from keyboards import get_create, get_keyboard, get_cancel


bot = Bot(API_TOKEN)
dp = Dispatcher(bot=bot)


class TestMiddleware(BaseMiddleware):

    async def on_process_update(self, update, data):
        print("qwertyuiop")

    async def on_pre_process_update(self, update: types.Update, data: dict):
        print("Hello")


@dp.message_handler(commands=["start"])
async def handle_start_command(message: types.Message) -> None:
    await message.answer("✋ Assalomu alaykum, botimizga hush kelibsiz")
    await message.delete()
    print("world!")


if __name__ == "__main__":
    dp.middleware.setup(TestMiddleware())
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True,
        # on_startup=on_startup,
    )
