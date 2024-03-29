from aiogram import Dispatcher, Bot, executor, types
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from verbs import *
from config import API_TOKEN
from sqlite import start_db, create_profile, edit_profile
from keyboards import get_create, get_keyboard, get_cancel


async def on_startup(_):
    # Mavjud bo'lgan bazani boshlash
    await start_db()


# Xotira saqlash uchun MemoryStorage obyektini yaratish
storage = MemoryStorage()
bot = Bot(API_TOKEN)
dp = Dispatcher(bot=bot, storage=storage)


# Yangi FSM holat guruhini tuzish
class AnnouncementStatesGroup(StatesGroup):
    full_name = State()
    skills = State()
    phone_number = State()
    time = State()
    goal = State()


# Yangi xabarlar uchun mulohazalar qabul qilish
@dp.message_handler(Text(equals="⬅️ Bekor qilish"), state="*")
async def handle_start_command(message: types.Message, state: FSMContext) -> None:
    if state is None:
        return

    # Holatni yakunlash va foydalanuvchiga javob berish
    await state.finish()
    await message.answer(
        "Jarayon toxtatildi!",
        reply_markup=get_create(),
    )


# /start buyrug'iga javob berish
@dp.message_handler(commands=["start"])
async def handle_start_command(message: types.Message) -> None:
    # Bosh sahifani ko'rsatish va foydalanuvchi profilini yaratish
    await message.answer(START_MESSAGE, reply_markup=get_keyboard(), parse_mode="html")
    await message.delete()
    await create_profile(user_id=message.from_user.id)


# 'Loyiha kerak' xabari uchun mulohazalarni qabul qilish
@dp.message_handler(Text(equals="Loyiha kerak"))
async def handle_loyiha_kerak(message: types.Message) -> None:
    await message.answer(LOYIHA_KERAK, parse_mode="html")
    await message.answer(
        "<b>Ism va familyangizni kiriting.</b>",
        reply_markup=get_cancel(),
        parse_mode="html",
    )
    await AnnouncementStatesGroup.full_name.set()


# Ism va familya ma'lumotlarini qabul qilish
@dp.message_handler(state=AnnouncementStatesGroup.full_name)
async def handle_load_fullname(message: types.Message, state: FSMContext) -> None:
    print("Ishladi")
    async with state.proxy() as data:
        data["full_name"] = message.text.title()

    await message.reply(TECHNOLOGY_MESSAGE, parse_mode="html")
    await AnnouncementStatesGroup.next()


# Texnologiya ma'lumotlarini qabul qilish
@dp.message_handler(state=AnnouncementStatesGroup.skills)
async def handle_load_skills(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data["skills"] = message.text

    await message.reply(PHONE_NUMBER, parse_mode="html")
    await AnnouncementStatesGroup.next()


# Telefon raqamini qabul qilish
@dp.message_handler(state=AnnouncementStatesGroup.phone_number)
async def handle_load_phonenumber(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data["phone_number"] = message.text

    await message.reply(TIME, parse_mode="html")
    await AnnouncementStatesGroup.next()


# Murojaat vaqti ma'lumotlarini qabul qilish
@dp.message_handler(state=AnnouncementStatesGroup.time)
async def handle_load_time(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data["time"] = message.text

    await message.reply(GOAL, parse_mode="html")
    await AnnouncementStatesGroup.next()


# Maqsad ma'lumotlarini qabul qilish va profilni yaratish
@dp.message_handler(state=AnnouncementStatesGroup.goal)
async def handle_load_description(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data["goal"] = message.text
        await bot.send_message(
            chat_id=message.from_user.id,
            text=f"""*Loyiha kerak*
    
👤 *Ism familyasi:* {data['full_name']}
📚 *Texnologiya:* {data['skills']}
🇺🇿 *Telegram: @{message.from_user.username}*  
📞 *Telefon:* {data['phone_number']}
🕰 *Murojaat qilish vaqti:* {data['time']}
🔎 *Maqsadi:* {data['goal']}

📣 *E'lon berish: @uzbeklearnersbot *
💬 *Suhbat uchun guruh: @uzbek_learners_team*

#️⃣ *#elon  #loyiha_kerak  #elon*

*✨ @uzbek_learners ✨*""",
            parse_mode="markdown",
        )

    await edit_profile(state, user_id=message.from_user.id)

    await message.reply(
        "Ma'lumotlaringiz muvaffaqiyatli saqlandi, rahmat.",
        reply_markup=ReplyKeyboardRemove(),
    )
    await state.finish()


# Asosiy funksiyani ishga tushirish
if __name__ == "__main__":
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True,
        on_startup=on_startup,
    )
