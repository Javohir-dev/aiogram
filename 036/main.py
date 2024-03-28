from aiogram import Dispatcher, Bot, executor, types
from aiogram.dispatcher.middlewares import BaseMiddleware

from config import API_TOKEN

bot = Bot(API_TOKEN)
dp = Dispatcher(bot=bot)

def set_key(key: str = None):
    def decorator(func):
        setattr(func, 'key', key)

        return func

    return decorator

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


@dp.message_handler(lambda message: message.text.lower() == "salom")
async def handle_salom(message: types.Message) -> None:
    await message.answer("Sizga ham salom!")

if __name__ == "__main__":
    # dp.middleware.setup(CustomMiddleware())
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True,
        # on_startup=on_startup,
    )
