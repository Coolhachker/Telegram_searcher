from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import re

from src.tg_bot.Configs.name_of_buttons import NamesOfButtons
from src.tg_bot.Configs import templates
from src.tg_bot.keyboards.chats_keyboard import return_keyboard_about_chats
from src.tg_bot.keyboards.start_keyboard import return_start_keyboard
from src.tg_bot.keyboards.key_words_keyboard import return_key_words_keyboard
from src.tg_bot.keyboards.turn_parser import return_turn_keyboard

from databases.sqlite import sqlite3_client

from src.tg_bot.Configs.templates import parser_is_working_message, parser_isnt_working_message


def handle_texts(dispatcher: Dispatcher, bot: Bot):
    @dispatcher.message(lambda message: re.search(NamesOfButtons.reply_button_chats, message.text))
    async def handle_reply_button_chats(message: Message):
        await bot.send_message(message.chat.id, templates.message_for_actions_over_chats, reply_markup=return_keyboard_about_chats())

    @dispatcher.message(lambda message: re.search(NamesOfButtons.comeback_button, message.text))
    async def handler_comeback(message: Message, state: FSMContext):
        await state.clear()
        await bot.send_message(message.chat.id, templates.comeback_message, reply_markup=return_start_keyboard())

    @dispatcher.message(lambda message: re.search(NamesOfButtons.key_words_button, message.text))
    async def handle_key_words(message: Message):
        await bot.send_message(message.chat.id, templates.message_for_actions_over_key_words, reply_markup=return_key_words_keyboard())

    @dispatcher.message(lambda message: re.search(NamesOfButtons.parser_button, message.text))
    async def handle_parser_button(message: Message):
        pid = sqlite3_client.get_pid()
        if pid is None or pid == 0:
            await bot.send_message(message.chat.id, parser_isnt_working_message, reply_markup=return_turn_keyboard(False))
        else:
            await bot.send_message(message.chat.id, parser_is_working_message, reply_markup=return_turn_keyboard(True))
