from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.keyboards.inline_buttons.inline_button import InlineButton

cancel_keyboard = InlineKeyboardBuilder()

cancel_keyboard.row(InlineButton.cancel_button)
