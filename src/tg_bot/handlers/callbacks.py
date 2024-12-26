from aiogram import Dispatcher, Bot
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

import re

from src.tg_bot.Configs.name_of_callbacks import NameOfCallbacks
from src.tg_bot.Configs.States import States
from src.tg_bot.Configs.templates import \
(
     get_url_message,
     comeback_message,
     get_key_word_message,
)

from src.tg_bot.keyboards.comeback_keyboard import return_comeback_keyboard
from src.tg_bot.keyboards.chats_keyboard import return_keyboard_about_chats
from src.tg_bot.keyboards.key_words_keyboard import return_key_words_keyboard

from src.tg_bot.handlers.callback_under_functions.delete_chats import return_delete_chats_functions
from src.tg_bot.handlers.callback_under_functions.delete_key_words import return_delete_functions_for_key_words
from src.tg_bot.handlers.callback_under_functions.change_key_words import return_functions_for_change_key_word


def handle_callbacks(dispatcher: Dispatcher, bot: Bot):
    return_delete_chats_functions(dispatcher, bot)
    return_delete_functions_for_key_words(dispatcher, bot)
    return_functions_for_change_key_word(dispatcher, bot)

    @dispatcher.callback_query(lambda cq: NameOfCallbacks.callback_for_add_chat_button == cq.data)
    async def handle_callback_on_add_chat(cq: CallbackQuery, state: FSMContext):
        await state.set_state(States.get_url_of_chat)
        await bot.send_message(cq.message.chat.id, get_url_message, reply_markup=return_comeback_keyboard())

    @dispatcher.callback_query(lambda cq: re.search(NameOfCallbacks.callback_for_comeback_button, cq.data))
    async def handle_callback_on_comeback_button(cq: CallbackQuery):
        if re.search('chat', cq.data):
            await bot.send_message(cq.message.chat.id, comeback_message, reply_markup=return_keyboard_about_chats())
        elif re.search('key_word', cq.data):
            await bot.send_message(cq.message.chat.id, comeback_message, reply_markup=return_key_words_keyboard())

    @dispatcher.callback_query(lambda cq: NameOfCallbacks.callback_for_add_key_word_button == cq.data)
    async def handle_callback_on_add_key_word_button(cq: CallbackQuery, state: FSMContext):
        await state.set_state(States.get_key_word)
        await bot.send_message(cq.message.chat.id, get_key_word_message, reply_markup=return_comeback_keyboard())

