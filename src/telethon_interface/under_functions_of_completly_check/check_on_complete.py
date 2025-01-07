from telethon import TelegramClient
from telethon.types import Message
import logging

from databases.sqlite import sqlite3_client

from src.telethon_interface.real_time_processing import realtime_processing

logger = logging.getLogger()


async def check_on_complete(message: Message, url: str, client: TelegramClient):
    if message.id == 1:
        sqlite3_client.update_check_completely(url)
        logger.info(f'Стартует real time проверка url - {url}')
        await realtime_processing(url, client)