import requests
from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.utils.formatting import Text, Bold

from bot.config import settings
from bot.keyboards.keyboard_from_start import keyboard_for_start

start_router = Router()
url_web = settings.url_web.get_secret_value()


@start_router.message(CommandStart())
async def cmd_hello(message: types.Message):
    answer = await send_post_request()
    content = Text("Hello, ", Bold(message.from_user.full_name), answer)
    await message.answer(
        **content.as_kwargs(),
        reply_markup=keyboard_for_start.as_markup(resize_keyboard=True)
    )
    await message.delete()


async def send_post_request():
    url = url_web + "/hook"
    value1 = 10
    value2 = 20
    payload = {"key1": value1, "key2": value2}
    response = requests.post(url, json=payload)
    return response.json()
