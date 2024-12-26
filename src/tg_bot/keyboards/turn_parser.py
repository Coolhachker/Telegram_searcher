from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, InlineKeyboardMarkup

from src.tg_bot.Configs.name_of_buttons import NamesOfButtons
from src.tg_bot.Configs.name_of_callbacks import NameOfCallbacks


def return_turn_keyboard(state_of_parser: bool) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    turn_on_button = InlineKeyboardButton(text=NamesOfButtons.turn_on_button, callback_data=NameOfCallbacks.turn_on_parser)
    turn_off_button = InlineKeyboardButton(text=NamesOfButtons.turn_off_parser, callback_data=NameOfCallbacks.turn_off_parser)

    if state_of_parser:
        builder.row(turn_off_button)
    else:
        builder.row(turn_on_button)

    return builder.as_markup()