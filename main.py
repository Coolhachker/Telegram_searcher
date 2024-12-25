import asyncio

from src.tg_bot.bot_engine import BotEngine


if __name__ == '__main__':
    bot_engine = BotEngine()
    asyncio.run(bot_engine.run())