from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup, KeyboardButton
from src.tg_bot.Configs.name_of_buttons import NamesOfButtons


def return_start_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    button_chats = KeyboardButton(text=NamesOfButtons.reply_button_chats)
    button_key_words = KeyboardButton(text=NamesOfButtons.key_words_button)
    button_parser = KeyboardButton(text=NamesOfButtons.parser_button)

    builder.row(button_chats)
    builder.row(button_key_words)
    builder.row(button_parser)

    return builder.as_markup(resize_keyboard=True)