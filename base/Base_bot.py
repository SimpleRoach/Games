from aiogram import Bot, Dispatcher, F
import asyncio
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

bot = Bot(token='6757514713:AAFbwHmv4BZMHHtqkf9WBA2YsDNEUbsHHgc')
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Старт')
    await message.reply('Отвечаю')

@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Нажато help')




async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')

# executor.start_polling(dp, skip_updates=True)