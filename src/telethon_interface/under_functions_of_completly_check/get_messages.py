from telethon import TelegramClient
from telethon.types import Message
import logging
import time

from databases.sqlite import sqlite3_client

logger = logging.getLogger()


async def get_messages(client: TelegramClient, url: str) -> (list[Message], list):
    logger.info(f'Начало итерации - {url}')
    message_id = sqlite3_client.get_id_of_message(url)
    ban_list = sqlite3_client.get_ban_members()

    logger.info(f'Получение фактических переменных с бд - {url}')
    logger.info(f'фактическое пост id = {message_id} у url - {url}')

    time.sleep(.4)
    messages = await client.get_messages(url, offset_id=message_id, limit=15)
    logger.info(f'Получение сообщений - {url}')

    return messages, ban_list