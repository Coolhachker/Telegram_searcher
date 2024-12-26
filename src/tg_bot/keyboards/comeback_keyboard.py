from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton, ReplyKeyboardMarkup

from src.tg_bot.Configs.name_of_buttons import NamesOfButtons


def return_comeback_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    comeback_button = KeyboardButton(text=NamesOfButtons.comeback_button)

    builder.row(comeback_button)

    return builder.as_markup(resize_keyboard=True)