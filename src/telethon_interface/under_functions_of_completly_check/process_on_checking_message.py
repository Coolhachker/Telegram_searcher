from telethon.types import Message, User
import logging
import time

from src.telethon_interface.check_message import check_message

logger = logging.getLogger()


async def process_message(message: Message, data_of_chat: dict, url: str, ban_list: list, entity_of_user: User):
    try:
        if isinstance(message, Message) and check_message(message.message) and entity_of_user.username not in ban_list:
            logger.info(f'пройдено условие - {url}')

            data_of_chat['message'] = f"Сообщение - {message.message}\nИз чата - {url} \n"
            data_of_chat["message"] += f"Ссылка на сообщение - https://t.me/c/{message.peer_id.channel_id}/{message.id}"
    except TypeError as _ex:
        logger.error(f'Получил ошибку {TypeError} по url = {url}:', exc_info=_ex)

    except AttributeError as _ex:
        logger.error(f'Получил ошибку {AttributeError} по url = {url}')

    return data_of_chat