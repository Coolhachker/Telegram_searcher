from telethon.types import Message, User
import logging
import time

from src.telethon_interface.check_message import check_message

from databases.sqlite import sqlite3_client

logger = logging.getLogger()


async def process_message(message: Message, url: str, ban_list: list, entity_of_user: User):
    try:
        if isinstance(message, Message) and check_message(message.message) and entity_of_user.username not in ban_list:
            logger.info(f'пройдено условие - {url}')

            message_text = f"""Сообщение - {message.message}\nИз чата - {url} \n"""
            message_text += f"""Ссылка на сообщение - https://t.me/c/{message.peer_id.channel_id}/{message.id}"""

            sqlite3_client.update_message(url, message_text)
    except TypeError as _ex:
        logger.error(f'Получил ошибку {TypeError} по url = {url}:', exc_info=_ex)

    except AttributeError as _ex:
        logger.error(f'Получил ошибку {AttributeError} по url = {url}')
