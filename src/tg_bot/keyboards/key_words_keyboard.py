from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, InlineKeyboardMarkup

from src.tg_bot.Configs.name_of_buttons import NamesOfButtons
from src.tg_bot.Configs.name_of_callbacks import NameOfCallbacks


def return_key_words_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    add_key_word_button = InlineKeyboardButton(text=NamesOfButtons.add_key_world_button, callback_data=NameOfCallbacks.callback_for_add_key_word_button)
    delete_key_word_button = InlineKeyboardButton(text=NamesOfButtons.delete_key_world_button, callback_data=NameOfCallbacks.callback_for_delete_key_word_button)
    change_key_word_button = InlineKeyboardButton(text=NamesOfButtons.change_key_world_button, callback_data=NameOfCallbacks.callback_for_change_key_word_button)

    builder.row(add_key_word_button)
    builder.row(delete_key_word_button)
    builder.row(change_key_word_button)

    return builder.as_markup()