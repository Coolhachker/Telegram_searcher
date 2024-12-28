from telethon import TelegramClient
from telethon.types import Message
import logging
import time

from src.json_buffer.Json_engine import JsonEngine
from databases.sqlite import sqlite3_client

logger = logging.getLogger()


def save_message_id(url: str, data_of_chat: dict, json_data: dict, message: Message):

    data_of_chat['id'] = message.id
    json_data[url] = data_of_chat
    JsonEngine.write(url, json_data[url])
    logger.info(f'Сохранил message_id = {message.id} у url = {url}')