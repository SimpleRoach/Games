from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


class ResetStates(StatesGroup):
    name = State()
    game = State()
