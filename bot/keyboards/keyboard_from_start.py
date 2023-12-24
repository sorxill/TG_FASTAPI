from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder

keyboard_for_start = ReplyKeyboardBuilder()
keyboard_for_start.row(
    types.KeyboardButton(text="Регистрация"),
    types.KeyboardButton(text="Профиль"),
)

keyboard_for_start.row(
    types.KeyboardButton(
        text="Начать игру", request_poll=types.KeyboardButtonPollType(type="start_quiz")
    ),
)

keyboard_for_start.row(
    types.KeyboardButton(text="Связь с разработчиком"),
)
