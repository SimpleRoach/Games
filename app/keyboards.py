from aiogram.types import (ReplyKeyboardMarkup,
                           KeyboardButton,
                           InlineKeyboardMarkup,
                           InlineKeyboardButton)

from aiogram.utils.keyboard import (ReplyKeyboardBuilder,
                                    InlineKeyboardBuilder)


main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Крестики - Нолики')],
                                       [KeyboardButton(text='Камень - Ножницы - Бумага')],
                                       [KeyboardButton(text='Статистика'),
                                       KeyboardButton(text='Стоп')]],
                           resize_keyboard=True,input_field_placeholder='Выбери команду')

tictak = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Старт', callback_data='ticGame')]])

rock_ = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Старт', callback_data='rockGame')]])

rock_Game = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Камень'),
                                          KeyboardButton(text='Ножницы'),
                                          KeyboardButton(text='Бумага')],
                                          [KeyboardButton(text='Стоп Игра')]],
                                resize_keyboard=True,input_field_placeholder='Выбери команду')

tictak_Game1 = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Стоп Игра')]],
                                   resize_keyboard=True,input_field_placeholder='Выбери команду')