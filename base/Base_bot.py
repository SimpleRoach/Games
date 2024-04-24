from aiogram import Bot, Dispatcher
from aiogram.dispatcher import router
import asyncio


bot = Bot(token='6757514713:AAFbwHmv4BZMHHtqkf9WBA2YsDNEUbsHHgc')
dp = Dispatcher()

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())


# executor.start_polling(dp, skip_updates=True)