###################################################################################
###################################################################################
# Создать в текущей папке .env файл и записать в него ключ значение BOT_TOKEN=""###
###################################################################################
###################################################################################
import asyncio

from aiogram import Dispatcher, Bot
import os
from dotenv import load_dotenv

from src.tg_bot.handlers import commands, texts, callbacks, states
from src.tg_bot.middlewarse.middleware_filter_from_other_users import MiddlewareFilterForAdmin
from src.tg_bot.middlewarse.middleware_on_callback_request import MiddlewareOnCallback
from src.tg_bot.handlers.handler_of_new_messages_from_parser import handle_new_messages_from_parser
load_dotenv()


class BotEngine:
    def __init__(self):
        self.bot = Bot(os.getenv('BOT_TOKEN'))
        self.dispatcher = Dispatcher()
        self.run_sync_functions()

    def run_sync_functions(self):
        commands.handle_commands(self.dispatcher, self.bot)
        texts.handle_texts(self.dispatcher, self.bot)
        callbacks.handle_callbacks(self.dispatcher, self.bot)
        states.handle_states(self.dispatcher, self.bot)

    async def run(self):
        asyncio.create_task(handle_new_messages_from_parser(self.bot))
        self.dispatcher.message.middleware(MiddlewareFilterForAdmin(self.bot))
        self.dispatcher.callback_query.middleware(MiddlewareOnCallback(self.bot))
        await self.dispatcher.start_polling(self.bot)


