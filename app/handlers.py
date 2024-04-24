from aiogram import  Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
import app.keyboards as kb


router = Router()
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Старт', reply_markup=kb.main)
    await message.reply('Отвечаю')


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Нажато help')
