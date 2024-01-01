from aiogram.fsm.state import StatesGroup, State


class RegistrationState(StatesGroup):
    choosing_username = State()
