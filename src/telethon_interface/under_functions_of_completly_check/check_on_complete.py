from telethon import TelegramClient
from telethon.types import Message
import logging

from src.json_buffer.Json_engine import JsonEngine

from src.telethon_interface.real_time_processing import realtime_processing

logger = logging.getLogger()


async def check_on_complete(message: Message, data_of_chat: dict, json_data: dict, url: str, client: TelegramClient):
    if message.id == 1:
        data_of_chat['check_completely'] = 1
        json_data[url] = data_of_chat
        JsonEngine.write(url, json_data[url])

        logger.info(f'Стартует real time проверка url - {url}')
        await realtime_processing(url, client)