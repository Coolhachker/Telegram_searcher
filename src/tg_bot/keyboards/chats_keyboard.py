from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup, InlineKeyboardButton

from src.Configs.name_of_buttons import NamesOfButtons
from src.Configs.name_of_callbacks import NameOfCallbacks


def return_keyboard_about_chats() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    button_add_chat = InlineKeyboardButton(text=NamesOfButtons.add_chat_button, callback_data=NamesOfButtons.add_chat_button)
    button_delete_button = InlineKeyboardButton(text=NamesOfButtons.delete_chat_button, callback_data=NameOfCallbacks.callback_for_delete_chat_button)

    builder.row(button_add_chat)
    builder.row(button_delete_button)

    return builder.as_markup()