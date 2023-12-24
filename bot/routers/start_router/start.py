from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.utils.formatting import Text, Bold

from bot.keyboards.keyboard_from_start import keyboard_for_start

start_router = Router()


@start_router.message(CommandStart())
async def cmd_hello(message: types.Message):
    content = Text("Hello, ", Bold(message.from_user.full_name))
    await message.answer(
        **content.as_kwargs(),
        reply_markup=keyboard_for_start.as_markup(resize_keyboard=True)
    )
    await message.delete()
