from aiogram import Dispatcher, Bot
from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardBuilder

import re

from src.tg_bot.Configs.name_of_callbacks import NameOfCallbacks
from src.tg_bot.Configs.name_of_buttons import NamesOfButtons
from src.tg_bot.Configs.templates import \
(
     message_for_choose_delete_key_word,
     message_on_success_key_word_delete
)

from databases.sqlite import sqlite3_client


def return_delete_functions_for_key_words(dispatcher: Dispatcher, bot: Bot):
    @dispatcher.callback_query(lambda cq: NameOfCallbacks.callback_for_delete_key_word_button == cq.data)
    async def handle_callback_on_delete_key_word_button(cq: CallbackQuery, count: int = 0):
        key_words = sqlite3_client.get_key_words()
        buttons: list[InlineKeyboardButton] = []
        builder = InlineKeyboardBuilder()
        button_comeback = InlineKeyboardButton(text=NamesOfButtons.comeback_button, callback_data=NameOfCallbacks.callback_for_comeback_button+"key_word")
        right_button = InlineKeyboardButton(text=NamesOfButtons.right_button, callback_data=NameOfCallbacks.callback_for_right_button_key_words + f'{count}')
        left_button = InlineKeyboardButton(text=NamesOfButtons.left_button, callback_data=NameOfCallbacks.callback_for_left_button_key_words + f'{count}')

        for index, key_word in enumerate(key_words):
            if count <= index < 5 + count:
                buttons.append(InlineKeyboardButton(text=f'{index + 1}.' + key_word[0], callback_data=NameOfCallbacks.callback_for_delete_key_word_index_button + f'{index}'))

        for button in buttons:
            builder.row(button)

        builder.row(left_button, button_comeback, right_button)

        await bot.send_message(cq.message.chat.id, text=message_for_choose_delete_key_word, reply_markup=builder.as_markup())

    @dispatcher.callback_query(lambda cq: re.search(NameOfCallbacks.callback_for_right_button_key_words, cq.data))
    async def handle_callback_on_right_chat_button(cq: CallbackQuery):
        count = int(cq.data.split('=')[1])
        count += 5
        await handle_callback_on_delete_key_word_button(cq, count)

    @dispatcher.callback_query(lambda cq: re.search(NameOfCallbacks.callback_for_left_button_key_words, cq.data))
    async def handle_callback_on_left_chat_button(cq: CallbackQuery):
        count = int(cq.data.split('=')[1])
        count -= 5
        await handle_callback_on_delete_key_word_button(cq, count)

    @dispatcher.callback_query(lambda cq: re.findall(NameOfCallbacks.callback_for_delete_key_word_index_button, cq.data))
    async def handle_callback_on_delete_chat_button(cq: CallbackQuery):
        key_word = sqlite3_client.get_key_words()[int(cq.data.split('=')[1])][0]
        sqlite3_client.delete_key_word(key_word)

        await bot.send_message(cq.message.chat.id, message_on_success_key_word_delete)