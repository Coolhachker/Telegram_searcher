import time

from telethon import TelegramClient
from telethon.types import User
import asyncio

from databases.sqlite import sqlite3_client

from src.telethon_interface.under_functions_of_completly_check.get_messages import get_messages
from src.telethon_interface.under_functions_of_completly_check.save_message_id import save_message_id
from src.telethon_interface.under_functions_of_completly_check.check_on_complete import check_on_complete
from src.telethon_interface.under_functions_of_completly_check.process_on_checking_message import process_message
from src.telethon_interface.under_functions_of_completly_check.wait_the_delete_message import wait_the_delete

import logging

logger = logging.getLogger()


async def complete_check(url: str, client: TelegramClient):
    logger.info(f'Функция начала работу с чатом - {url}')
    while True:
        try:
            list_of_messages, ban_list = await get_messages(client, url)
            for message in list_of_messages:
                await check_on_complete(message, url, client)

                await wait_the_delete(url)

                save_message_id(url, message)

                id_of_user = message.from_id.user_id
                time.sleep(.3)
                entity_of_user = await client.get_entity(id_of_user)
                entity_of_user = '' if not isinstance(entity_of_user, User) else entity_of_user
                logger.info(f"Получение данных из сообщения - {url}\nmessage_id={message.id}")

                await process_message(message, url, ban_list, entity_of_user)

                logger.info(f'Сохранил информацию: message_id = {message.id}, message_text = {sqlite3_client.get_message(url)}, check_completely = {sqlite3_client.get_check_completely(url)}')
                await asyncio.sleep(.1)

        except Exception as _ex:
            logger.error(f'Получил ошибку во внешней функции {complete_check} по url = {url}:', exc_info=_ex)
            await asyncio.sleep(.5)
