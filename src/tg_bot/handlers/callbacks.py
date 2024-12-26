from aiogram import Dispatcher, Bot
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

import re

from src.tg_bot.Configs.name_of_callbacks import NameOfCallbacks
from src.tg_bot.Configs.States import States
from src.tg_bot.Configs.templates import get_url_message

from src.tg_bot.keyboards.comeback_keyboard import return_comeback_keyboard


def handle_callbacks(dispatcher: Dispatcher, bot: Bot):
    @dispatcher.callback_query(lambda cq: NameOfCallbacks.callback_for_add_chat_button == cq.data)
    async def handle_callback_on_add_chat(cq: CallbackQuery, state: FSMContext):
        await state.set_state(States.get_url_of_chat)
        await bot.send_message(cq.message.chat.id, get_url_message, reply_markup=return_comeback_keyboard())
