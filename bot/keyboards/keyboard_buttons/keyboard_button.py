from aiogram import types


class KeyButton:
    register = types.KeyboardButton(text="Register")
    profile = types.KeyboardButton(text="Profile")
    quiz_game = types.KeyboardButton(
        text="Start Quiz",
        request_poll=types.KeyboardButtonPollType(type="quiz"),
    )
    contacts_with_dev = types.KeyboardButton(text="Developer contacts")
