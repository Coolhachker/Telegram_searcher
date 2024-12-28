from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, InlineKeyboardMarkup
from src.tg_bot.Configs.name_of_buttons import NamesOfButtons
from src.tg_bot.Configs.name_of_callbacks import NameOfCallbacks


def return_ban_list_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    add_member_into_ban_list_button = InlineKeyboardButton(text=NamesOfButtons.add_member_into_ban_list_button, callback_data=NameOfCallbacks.callback_for_add_member_into_ban_list_button)
    delete_member_from_ban_list_button = InlineKeyboardButton(text=NamesOfButtons.delete_member_from_ban_list_button, callback_data=NameOfCallbacks.callback_for_delete_member_from_ban_list_button)

    builder.row(add_member_into_ban_list_button)
    builder.row(delete_member_from_ban_list_button)

    return builder.as_markup()

