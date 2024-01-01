from aiogram import Router, types, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from bot.fsm_states.registration_states import RegistrationState
from bot.keyboards.all_keyboards.keyboard_for_cancel import cancel_keyboard

register_router = Router()


@register_router.message(StateFilter(None), F.text == "Register")
async def cmd_hello(message: types.Message, state: FSMContext):
    await message.answer(
        text="Введите ваш никнейм: ",
        reply_markup=cancel_keyboard.as_markup(),
    )
    await state.set_state(RegistrationState.choosing_username)
