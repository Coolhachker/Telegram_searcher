from aiogram import Dispatcher, Bot
import os
from dotenv import load_dotenv

from src.tg_bot.handlers import commands, texts
from src.tg_bot.middlewarse.middleware_filter_from_other_users import MiddlewareFilterForAdmin

load_dotenv()


class BotEngine:
    def __init__(self):
        self.bot = Bot(os.getenv('BOT_TOKEN'))
        self.dispatcher = Dispatcher()
        self.run_sync_functions()

    def run_sync_functions(self):
        commands.handle_commands(self.dispatcher, self.bot)
        texts.handle_texts(self.dispatcher, self.bot)

    async def run(self):
        self.dispatcher.message.middleware(MiddlewareFilterForAdmin(self.bot))
        await self.dispatcher.start_polling(self.bot)

