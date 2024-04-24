from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Крестики - Нолики')],
                                       [KeyboardButton(text='Камень - Ножницы - Бумага')],
                                       [KeyboardButton(text='Статистика')],
                                       [KeyboardButton(text='Стоп')]])
