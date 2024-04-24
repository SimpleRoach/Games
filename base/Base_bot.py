from aiogram import Bot, Dispatcher
import asyncio
from aiogram.types import Message


bot = Bot(token='6757514713:AAFbwHmv4BZMHHtqkf9WBA2YsDNEUbsHHgc')
dp = Dispatcher()

@dp.message()
async def cmd_start(message: Message):
    await message.answer('Старт')
    await message.reply('Отвечаю')




async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())


# executor.start_polling(dp, skip_updates=True)