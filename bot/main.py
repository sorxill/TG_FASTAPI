import asyncio
import logging

from aiogram import Bot, Dispatcher

from bot.routers.cancel_script import cancel_router
from bot.routers.registration_router.register import register_router
from config import settings
from routers.start_router.start import start_router

bot = Bot(token=settings.bot_token.get_secret_value(), parse_mode="HTML")
dp = Dispatcher()
dp.include_router(start_router)
dp.include_router(register_router)
dp.include_router(cancel_router)


async def on_startup():
    await bot.set_webhook(url=settings.url_web.get_secret_value())


async def on_shutdown():
    logging.warning("Shutting down..")


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot, on_startup=on_startup, on_shutdown=on_shutdown)


if __name__ == "__main__":
    asyncio.run(main())
