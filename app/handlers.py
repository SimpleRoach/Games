from aiogram import  F, Router, Bot
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


@router.message(F.text == 'Крестики - Нолики')
async def tic_tac(message: Message):
    photo = './app/ttic.jpeg'
    text = 'Выбрана игра "Крестики - Нолики"'
    await message.answer(text, reply_markup=kb.tictak)


@router.message(F.text == 'Камень - Ножницы - Бумага')
async def Rock_paper_scissors(message: Message):
    text = 'Выбрана игра "Камень - Ножницы - Бумага"'
    await message.answer(text, reply_markup=kb.rock_)