import asyncio
import datetime
import logging
from aiogram.client.default import DefaultBotProperties
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters.command import Command
from aiogram.enums import ParseMode
from config import API_BOT1_KEY,API_BOT2_KEY
from functions import auth, deleteprovided, get_button_manicure_basic, getdatatday, getmonth, parser

from apscheduler.schedulers.asyncio import AsyncIOScheduler


logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s %(levelname)s %(message)s"
    )

scheduler = AsyncIOScheduler()


bot = Bot(token=API_BOT1_KEY,
          default=DefaultBotProperties(parse_mode=ParseMode.HTML))
#bot2 = Bot(token=API_BOT2_KEY,
#          default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()




base_servise = []



# Хэндлер на команду /start
@dp.message(Command("start", "menu"))
@auth
async def cmd_start(message: types.Message):
    answer, kb = get_button_manicure_basic()
    keyboards = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer(answer, reply_markup=keyboards)


@dp.message(lambda message: message.text.startswith('/del'))
@auth
async def del_provided(message: types.Message):
    row_id = int(message.text[4:])
    answer = deleteprovided(row_id)
    await message.answer(answer)


@dp.message(Command("today"))
@auth
async def cmd_start(message: types.Message):
    today = datetime.date.today()
    answer = getdatatday(today, message.from_user.id)
    await message.answer(answer)

@dp.message(Command("month"))
@auth
async def cmd_start(message: types.Message):
    today = datetime.date.today()
    answer = getmonth(today, message.from_user.id)
    await message.answer(answer, parse_mode="html")

@dp.message(Command("last_month"))
@auth
async def cmd_start(message: types.Message):
    today = datetime.date.today()
    last_day = datetime.date.today() - datetime.timedelta(days=today.day+1)

    answer = getmonth(last_day, message.from_user.id)
    await message.answer(answer)
@auth
@dp.message(Command("help"))
async def cmd_start(message: types.Message):
    print(message)
    await message.answer("Help!")


@dp.message()
@auth
async def cmd_start(message: types.Message):
    answer, kb = parser(message)
    keyboards = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer(answer, reply_markup=keyboards)


async def message_reminder():
    await bot.send_message(775094528, "Привет! Это Я.")


#----------------------------


scheduler.add_job(
    message_reminder, 
    'cron', 
    hour=22, 
    minute=0, 
    start_date=datetime.datetime.today()
    )


# Запуск процесса поллинга новых апдейтов
async def main():
    scheduler.start()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
