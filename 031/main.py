from aiogram import Dispatcher, Bot, executor, types
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage


from config import API_TOKEN

# from keyboards import get_keyboard, get_cancel

storage = MemoryStorage()
bot = Bot(API_TOKEN)
dp = Dispatcher(bot=bot, storage=storage)


class ProfileStatesGroup(StatesGroup):
    photo = State()
    name = State()
    age = State()
    description = State()


@dp.message_handler(commands=["start"])
async def handle_start_command(message: types.Message) -> None:
    await message.answer("Salom!\nMa'lumotingizni kiritish uchun /create ga bosing.")
    await message.delete()


@dp.message_handler(commands=["create"])
async def handle_create_command(message: types.Message) -> None:
    await message.answer("Jarayonni boshlaymiz.")
    await message.answer("Birinchi bo'lib o'zingizni 🖼rasmingizni yuboring.")
    await ProfileStatesGroup.photo.set()


@dp.message_handler(content_types=["photo"], state=ProfileStatesGroup.photo)
async def handle_load_photo(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data["photo"] = message.photo[0].file_id

    await message.reply("Endi ismingizni kiriting.")
    await ProfileStatesGroup.next()


@dp.message_handler(state=ProfileStatesGroup.name)
async def handle_load_name(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data["name"] = message.text.title()

    await message.reply("Endi yoshingizni kiriting.")
    await ProfileStatesGroup.next()


@dp.message_handler(state=ProfileStatesGroup.age)
async def handle_load_age(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        try:
            data["age"] = int(message.text)
        except:
            await message.reply("Yosh butun sondan iborat bo'ladi havariz bormi?")

    await message.reply(
        "O'zingiz haqingizda ba'zi ma'lumotlarni yozib qoldiring, iltimos."
    )
    await ProfileStatesGroup.next()


@dp.message_handler(state=ProfileStatesGroup.description)
async def handle_load_description(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data["description"] = message.text
        await bot.send_photo(
            chat_id=message.from_user.id,
            photo=data["photo"],
            caption=f"{data['name']} | {data['age']}\n\n{data['description']}",
        )

    await message.reply("Ma'lumotlaringiz muvaffaqiyatli saqlandi, rahmat.")
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True)
