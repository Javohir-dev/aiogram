from aiogram import Dispatcher, Bot, executor, types
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage


from config import API_TOKEN
from keyboards import get_keyboard, get_cancel

storage = MemoryStorage()
bot = Bot(API_TOKEN)
dp = Dispatcher(bot=bot, storage=storage)


class ClientStatesGroup(StatesGroup):
    photo = State()
    desc = State()


@dp.message_handler(commands=["start"])
async def handle_start_command(message: types.Message) -> None:
    await message.answer(text="Welcome to my BOT", reply_markup=get_keyboard())
    await message.delete()


@dp.message_handler(Text(equals="⬅️ Bekor qilish"), state="*")
async def handle_start_command(message: types.Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return

    await message.reply("⚠ Bekor qilindi", reply_markup=get_keyboard())
    await state.finish()


@dp.message_handler(Text(equals="Ishni boshlash.", ignore_case=True), state=None)
async def handle_get_start(message: types.Message) -> None:
    await ClientStatesGroup.photo.set()
    await message.answer("Rasmni yuborishingiz mumkin.", reply_markup=get_cancel())


@dp.message_handler(lambda message: not message.photo, state=ClientStatesGroup.photo)
async def handle_check_photo(message: types.Message) -> None:
    return await message.reply("It is not photo!\nCheck it and try again.")


@dp.message_handler(
    lambda message: message.photo,
    content_types=["photo"],
    state=ClientStatesGroup.photo,
)
async def handle_load_photo(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data["photo"] = message.photo[0].file_id

    await ClientStatesGroup.next()
    await message.reply("Send me description please.")


@dp.message_handler(state=ClientStatesGroup.desc)
async def handle_load_desc(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data["desc"] = message.text

    await message.reply("Your photo saved.")

    async with state.proxy() as data:
        await bot.send_photo(
            chat_id=message.from_user.id,
            photo=data["photo"],
            caption=data["desc"],
            reply_markup=ReplyKeyboardRemove(),
        )
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True)
