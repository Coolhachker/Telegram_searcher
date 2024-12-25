from aiogram import BaseMiddleware, Bot

from src.Configs.templates import prohibition_message


class MiddlewareFilterForAdmin(BaseMiddleware):
    def __init__(self, bot: Bot):
        super().__init__()
        self.bot = bot
        self.trust_users = ['CHT_VENDETTA']

    async def __call__(self, handler, event, data):
        if event.chat.username in self.trust_users:
            await handler(event, data)
        else:
            await self.bot.send_message(event.chat.id, prohibition_message)