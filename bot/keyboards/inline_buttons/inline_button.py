from aiogram import types


class InlineButton:
    cancel_button = types.InlineKeyboardButton(
        text="Вернуться в меню",
        callback_data="cancel",
    )
