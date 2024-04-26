from aiogram import  F, Router, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
from app.Rock_paper_scissors import rps
import app.stages


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


@router.callback_query(F.data == 'ticGame')
async def ticGame(callback: CallbackQuery):
    await callback.answer('Вы нажали Старт')
    await callback.message.answer('Играем в Крестики - Нолики', reply_markup=kb.tictak_Game1)
    await callback.message.answer('🤖', reply_markup=kb.tictak)

@router.callback_query(F.data == 'rockGame')
async def rockGame(callback: CallbackQuery):
    await callback.answer('Вы нажали Старт')
    await callback.message.answer('Играем в Камень - Ножницы - Бумага', reply_markup=kb.rock_Game)


@router.message(F.text == 'Камень')
async def rockPlay(message: Message):
    await message.answer(rps('Камень'))
@router.message(F.text == 'Ножницы')
async def rockPlay(message: Message):
    await message.answer(rps('Ножницы'))
@router.message(F.text == 'Бумага')
async def rockPlay(message: Message):
    await message.answer(rps('Бумага'))


@router.message(F.text == 'Камень - Ножницы - Бумага')
async def Rock_paper_scissors(message: Message):
    text = 'Выбрана игра "Камень - Ножницы - Бумага"'
    await message.answer(text, reply_markup=kb.rock_)


@router.message(F.text == 'Стоп Игра')
async def rockPlay(message: Message):
    await message.answer('Окей', reply_markup=kb.main)