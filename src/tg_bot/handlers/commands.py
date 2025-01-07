from aiogram import Dispatcher, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message

from src.tg_bot.Configs import templates
from src.tg_bot.keyboards.start_keyboard import return_start_keyboard

from databases.sqlite import sqlite3_client

from src.tg_bot.Configs.templates import hello_message_for_admin_chats


def handle_commands(dispatcher: Dispatcher, bot: Bot):
    @dispatcher.message(CommandStart())
    async def handle_command_start(message: Message):
        await bot.send_message(message.chat.id, templates.hello_message, reply_markup=return_start_keyboard())

    @dispatcher.message(lambda message: message.new_chat_members is not None and message.new_chat_members[0].username == 'Excomunicade_Bot')
    async def handle_on_new_admin_chat(message: Message):
        sqlite3_client.add_admin_chat(message.chat.id)
        await bot.send_message(message.chat.id, hello_message_for_admin_chats)