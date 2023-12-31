from aiogram.utils.keyboard import ReplyKeyboardBuilder

from bot.keyboards.keyboard_buttons.keyboard_button import KeyButton

keyboard_for_start = ReplyKeyboardBuilder()

keyboard_for_start.row(
    KeyButton.register,
    KeyButton.profile,
)

keyboard_for_start.row(
    KeyButton.quiz_game,
)

keyboard_for_start.row(
    KeyButton.contacts_with_dev,
)
