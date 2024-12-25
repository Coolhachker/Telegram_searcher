from aiogram import Bot, Dispatcher
from aiogram.types import Message
import re

from src.Configs.name_of_buttons import NamesOfButtons
from src.Configs import templates
from src.tg_bot.keyboards.chats_keyboard import return_keyboard_about_chats


def handle_texts(dispatcher: Dispatcher, bot: Bot):
    @dispatcher.message(lambda message: re.search(NamesOfButtons.reply_button_chats, message.text))
    async def handle_reply_button_chats(message: Message):
        await bot.send_message(message.chat.id, templates.message_for_actions_over_chats, reply_markup=return_keyboard_about_chats())
