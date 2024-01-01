from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from bot.keyboards.all_keyboards.keyboard_from_start import keyboard_for_start

cancel_router = Router()


@cancel_router.callback_query(F.data == "cancel")
async def cmd_cancel(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.answer(
        text="Действие отменено",
        reply_markup=keyboard_for_start.as_markup(),
    )
    await callback.answer()
