from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup, KeyboardButton
from src.tg_bot.Configs.name_of_buttons import NamesOfButtons


def return_start_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    button_chats = KeyboardButton(text=NamesOfButtons.reply_button_chats)

    builder.row(button_chats)

    return builder.as_markup(resize_keyboard=True)