from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "6434489869:AAEESi6PoTKyr6U9nP6ceMKk8tiB6A8TWUQ"

bot = Bot(API_TOKEN)
db = Dispatcher(bot)


@db.message_handler(commands=["start", "restart"])
async def welcome(message: types.Message):
    await message.reply("👋 Assalomu alaykum,\nBotimisga hush kelibsiz.")


@db.message_handler()
async def echo(message: types.Message):
    # await message.reply(text=message.text.title())
    if message.text.count(" ") >= 1:
        await message.reply(message.text.title())
    else:
        await message.reply(message.text.upper())


if __name__ == "__main__":
    executor.start_polling(db)
    # executor.start_polling(dp, skip_updates=True)
