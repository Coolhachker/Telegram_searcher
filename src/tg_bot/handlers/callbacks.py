from aiogram import Dispatcher, Bot
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardBuilder

import re

from src.tg_bot.Configs.name_of_callbacks import NameOfCallbacks
from src.tg_bot.Configs.name_of_buttons import NamesOfButtons
from src.tg_bot.Configs.States import States
from src.tg_bot.Configs.templates import \
(
     get_url_message,
     message_for_choose_delete_chat,
     message_on_success_chat_delete,
     comeback_message,
     get_key_word_message,
     message_for_choose_delete_key_word,
)

from src.tg_bot.keyboards.comeback_keyboard import return_comeback_keyboard

from databases.sqlite import sqlite3_client

from src.tg_bot.handlers.delete_chats import return_delete_chats_functions
from src.tg_bot.handlers.delete_key_words import return_delete_functions_for_key_words


def handle_callbacks(dispatcher: Dispatcher, bot: Bot):
    return_delete_chats_functions(dispatcher, bot)
    return_delete_functions_for_key_words(dispatcher, bot)

    @dispatcher.callback_query(lambda cq: NameOfCallbacks.callback_for_add_chat_button == cq.data)
    async def handle_callback_on_add_chat(cq: CallbackQuery, state: FSMContext):
        await state.set_state(States.get_url_of_chat)
        await bot.send_message(cq.message.chat.id, get_url_message, reply_markup=return_comeback_keyboard())

    @dispatcher.callback_query(lambda cq: NameOfCallbacks.callback_for_comeback_button == cq.data)
    async def handle_callback_on_comeback_button(cq: CallbackQuery):
        await bot.send_message(cq.message.chat.id, comeback_message)

    @dispatcher.callback_query(lambda cq: NameOfCallbacks.callback_for_add_key_word_button == cq.data)
    async def handle_callback_on_add_key_word_button(cq: CallbackQuery, state: FSMContext):
        await state.set_state(States.get_key_word)
        await bot.send_message(cq.message.chat.id, get_key_word_message, reply_markup=return_comeback_keyboard())

