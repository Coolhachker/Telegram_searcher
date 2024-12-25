from aiogram import Dispatcher, Bot
from aiogram.types import CallbackQuery

import re

from src.Configs.name_of_callbacks import NameOfCallbacks


def handle_callbacks(dispatcher: Dispatcher, bot: Bot):
    @dispatcher.callback_query(lambda cq: re.search(NameOfCallbacks.callback_for_add_chat_button, cq.data))
    async def handle_callback_on_add_chat(cq: CallbackQuery):
        pass