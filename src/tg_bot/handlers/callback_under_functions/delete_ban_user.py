from aiogram import Dispatcher, Bot
from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardBuilder

import re

from src.tg_bot.Configs.name_of_callbacks import NameOfCallbacks
from src.tg_bot.Configs.name_of_buttons import NamesOfButtons
from src.tg_bot.Configs.templates import \
(
    message_for_choose_delete_ban_user,
    message_on_success_ban_user_delete
)


from databases.sqlite import sqlite3_client


def return_delete_ban_users_functions(dispatcher: Dispatcher, bot: Bot):
    @dispatcher.callback_query(lambda cq: NameOfCallbacks.callback_for_delete_member_from_ban_list_button == cq.data)
    async def handle_callback_on_delete_member_from_ban_list(cq: CallbackQuery, count=0):
        ban_users = sqlite3_client.get_ban_members()
        buttons: list[InlineKeyboardButton] = []
        builder = InlineKeyboardBuilder()

        button_comeback = InlineKeyboardButton(text=NamesOfButtons.comeback_button, callback_data=NameOfCallbacks.callback_for_comeback_button+"ban_users")
        right_button = InlineKeyboardButton(text=NamesOfButtons.right_button, callback_data=NameOfCallbacks.callback_for_right_button_ban_list + f'{count}')
        left_button = InlineKeyboardButton(text=NamesOfButtons.left_button, callback_data=NameOfCallbacks.callback_for_left_button_ban_list + f'{count}')

        for index, ban_user in enumerate(ban_users):
            if count <= index < 5 + count:
                buttons.append(InlineKeyboardButton(text=f'{index + 1}.' + ban_user, callback_data=NameOfCallbacks.callback_for_delete_ban_list_index_button + f'{index}'))

        for button in buttons:
            builder.row(button)

        builder.row(left_button, button_comeback, right_button)

        await bot.send_message(cq.message.chat.id, text=message_for_choose_delete_ban_user, reply_markup=builder.as_markup())

    @dispatcher.callback_query(lambda cq: re.search(NameOfCallbacks.callback_for_right_button_ban_list, cq.data))
    async def handle_callback_on_right_ban_list_button(cq: CallbackQuery):
        count = int(cq.data.split('=')[1])
        count += 5
        await handle_callback_on_delete_member_from_ban_list(cq, count)

    @dispatcher.callback_query(lambda cq: re.search(NameOfCallbacks.callback_for_left_button_ban_list, cq.data))
    async def handle_callback_on_left_ban_list_button(cq: CallbackQuery):
        count = int(cq.data.split('=')[1])
        count -= 5
        await handle_callback_on_delete_member_from_ban_list(cq, count)

    @dispatcher.callback_query(lambda cq: re.findall(NameOfCallbacks.callback_for_delete_ban_list_index_button, cq.data))
    async def handle_callback_on_delete_chat_button(cq: CallbackQuery):
        ban_user = sqlite3_client.get_ban_members()[int(cq.data.split('=')[1])]
        sqlite3_client.delete_ban_member_from_table(ban_user)

        await bot.send_message(cq.message.chat.id, message_on_success_ban_user_delete)
        await handle_callback_on_delete_member_from_ban_list(cq)
