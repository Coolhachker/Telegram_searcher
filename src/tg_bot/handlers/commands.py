from aiogram import Dispatcher, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message

from src.tg_bot.Configs import templates
from src.tg_bot.keyboards.start_keyboard import return_start_keyboard


def handle_commands(dispatcher: Dispatcher, bot: Bot):
    @dispatcher.message(CommandStart())
    async def handle_command_start(message: Message):
        await bot.send_message(message.chat.id, templates.hello_message, reply_markup=return_start_keyboard())