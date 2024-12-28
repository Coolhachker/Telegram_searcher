from telethon import TelegramClient
from telethon.types import Message
import logging
import time

from src.json_buffer.Json_engine import JsonEngine
from databases.sqlite import sqlite3_client

logger = logging.getLogger()


async def get_messages(client: TelegramClient, url: str) -> (list[Message], list):
    logger.info(f'Начало итерации - {url}')
    json_data = JsonEngine.read()
    data_of_chat = json_data[url]

    ban_list = sqlite3_client.get_ban_members()
    logger.info(f'Получение фактических переменных с бд - {url}')
    logger.info(f'фактическое пост id = {data_of_chat["id"]} у url - {url}')

    time.sleep(.4)
    messages = await client.get_messages(url, offset_id=data_of_chat['id'], limit=15)
    logger.info(f'Получение сообщений - {url}')

    return messages, ban_list