import time

from telethon import TelegramClient
from telethon.types import User
import asyncio

from src.json_buffer.Json_engine import JsonEngine


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
                json_data = JsonEngine.read()
                data_of_chat = json_data[url]
                data_of_chat['message'] = ''

                await check_on_complete(message, data_of_chat, json_data, url, client)

                wait_the_delete(url)

                save_message_id(url, data_of_chat, json_data, message)

                id_of_user = message.from_id.user_id
                time.sleep(.3)
                entity_of_user = await client.get_entity(id_of_user)
                entity_of_user = '' if not isinstance(entity_of_user, User) else entity_of_user
                logger.info(f"Получение данных из сообщения - {url}\nmessage_id={message.id}")

                data_of_chat = await process_message(message, data_of_chat, url, ban_list, entity_of_user)

                json_data[url] = data_of_chat
                JsonEngine.write(url, json_data[url])
                logger.info(f'Вывел информацию {json_data[url]} в json структуру - {url}')
                await asyncio.sleep(.1)

        except Exception as _ex:
            logger.error(f'Получил ошибку во внешней функции {complete_check} по url = {url}:', exc_info=_ex)
            await asyncio.sleep(.5)
