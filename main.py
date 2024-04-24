from aiogram import Bot, Dispatcher
import asyncio
from app.handlers import router




async def main():

    bot = Bot(token='6757514713:AAFbwHmv4BZMHHtqkf9WBA2YsDNEUbsHHgc')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
