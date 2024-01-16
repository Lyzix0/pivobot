from apscheduler.schedulers.asyncio import AsyncIOScheduler
import serial
import asyncio
import logging
from aiogram import Dispatcher, Bot
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message


TOKEN = "6126064693:AAGZFAwgg20Z1ZSycEtCa-6nCJoA2ohgvTc"
s = serial.Serial("COM8", 9600)

dp = Dispatcher()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Приветствую! Это бот для оповещений взлома сейфа для моего проекта на arduino.")

admin = 957967269
data = None


async def get_data():
    current_data = s.read().decode()

    if current_data == "0":
        await bot.send_message(admin, "Кто-то пытается открыть твой сейф")
    elif current_data == "1":
        await bot.send_message(admin, "Кто-то открыл твой сейф")


async def main():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(get_data, "interval", seconds=4)
    print("Бот запущен!")
    scheduler.start()
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.getLogger("aiogram").setLevel(logging.WARNING)
    logging.getLogger("apscheduler").setLevel(logging.ERROR)
    asyncio.run(main())

