from aiogram import Dispatcher, Bot, executor, types
from aiogram.dispatcher.middlewares import BaseMiddleware

from config import API_TOKEN

bot = Bot(API_TOKEN)
dp = Dispatcher(bot=bot)


class CustomMiddleware(BaseMiddleware):

    async def on_pre_process_update(self, update: types.Update, data: dict):
        pass

    async def on_process_update(self, update: types.Update, data: dict):
        pass

    async def on_process_message(self, message: types.Message, data: dict):
        print("======================================================================")
        print(data, message)
        print("======================================================================")


@dp.message_handler(commands=["start"])
async def handle_start_command(message: types.Message) -> None:
    inline_keybord = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton("Some Command", callback_data="some_command")]
        ]
    )
    await message.answer(
        "✋ Assalomu alaykum, botimizga hush kelibsiz", reply_markup=inline_keybord
    )
    await message.delete()
    print("START")


if __name__ == "__main__":
    dp.middleware.setup(CustomMiddleware())
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True,
        # on_startup=on_startup,
    )
