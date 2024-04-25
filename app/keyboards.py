from aiogram.types import (ReplyKeyboardMarkup,
                           KeyboardButton,
                           InlineKeyboardMarkup,
                           InlineKeyboardButton)


main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Крестики - Нолики')],
                                       [KeyboardButton(text='Камень - Ножницы - Бумага')],
                                       [KeyboardButton(text='Статистика'),
                                       KeyboardButton(text='Стоп')]],
                           resize_keyboard=True,input_field_placeholder='Выбери команду')

tictak = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Старт', callback_data='ticGame')],
                                               [InlineKeyboardButton(text='Статистика', callback_data='ticStat')],
                                               [InlineKeyboardButton(text='Меню', callback_data='exitMain')]])

rock_ = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Старт', callback_data='rockGame')],
                                               [InlineKeyboardButton(text='Статистика', callback_data='rockStat')],
                                               [InlineKeyboardButton(text='Меню', callback_data='exitMain')]])