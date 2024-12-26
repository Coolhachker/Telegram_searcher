from aiogram import Dispatcher, Bot
from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardBuilder

import re

from src.tg_bot.Configs.name_of_callbacks import NameOfCallbacks
from src.tg_bot.Configs.name_of_buttons import NamesOfButtons
from src.tg_bot.Configs.templates import \
(
     message_for_choose_delete_chat,
     message_for_choose_delete_key_word,
)


from databases.sqlite import sqlite3_client


def return_delete_chats_functions(dispatcher: Dispatcher, bot: Bot):
    @dispatcher.callback_query(lambda cq: NameOfCallbacks.callback_for_delete_chat_button == cq.data)
    async def handle_callback_on_delete_chat(cq: CallbackQuery, count=0):
        chats = sqlite3_client.get_chats()
        buttons: list[InlineKeyboardButton] = []
        builder = InlineKeyboardBuilder()
        button_comeback = InlineKeyboardButton(text=NamesOfButtons.comeback_button, callback_data=NameOfCallbacks.callback_for_comeback_button)
        right_button = InlineKeyboardButton(text=NamesOfButtons.right_button, callback_data=NameOfCallbacks.callback_for_right_button_chats + f'{count}')
        left_button = InlineKeyboardButton(text=NamesOfButtons.left_button, callback_data=NameOfCallbacks.callback_for_left_button_chats + f'{count}')

        for index, chat in enumerate(chats):
            if count <= index < 5 + count:
                buttons.append(InlineKeyboardButton(text=f'{index + 1}.' + chat[2], callback_data=NameOfCallbacks.callback_for_delete_chat_index_button + f'{index}'))

        for button in buttons:
            builder.row(button)

        builder.row(left_button, button_comeback, right_button)

        await bot.send_message(cq.message.chat.id, text=message_for_choose_delete_chat, reply_markup=builder.as_markup())

    @dispatcher.callback_query(lambda cq: re.search(NameOfCallbacks.callback_for_right_button_chats, cq.data))
    async def handle_callback_on_right_chat_button(cq: CallbackQuery):
        count = int(cq.data.split('=')[1])
        count += 5
        await handle_callback_on_delete_chat(cq, count)

    @dispatcher.callback_query(lambda cq: re.search(NameOfCallbacks.callback_for_left_button_chats, cq.data))
    async def handle_callback_on_left_chat_button(cq: CallbackQuery):
        count = int(cq.data.split('=')[1])
        count -= 5
        await handle_callback_on_delete_chat(cq, count)

    @dispatcher.callback_query(lambda cq: re.search(NameOfCallbacks.callback_for_delete_chat_index_button, cq.data))
    async def handle_callback_on_delete_chat_button(cq: CallbackQuery):
        key_url = sqlite3_client.get_chats()[int(cq.data.split('=')[1])][2]
        sqlite3_client.delete_chat_from_table(key_url)

        await bot.send_message(cq.message.chat.id, message_for_choose_delete_key_word)