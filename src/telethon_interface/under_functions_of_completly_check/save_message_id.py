from telethon import TelegramClient
from telethon.types import Message
import logging
import time

from src.json_buffer.Json_engine import JsonEngine
from databases.sqlite import sqlite3_client

logger = logging.getLogger()


def save_message_id(url: str, message: Message):
    sqlite3_client.update_id_of_message(url, message.id)
    logger.info(f'Сохранил message_id = {message.id} у url = {url}')