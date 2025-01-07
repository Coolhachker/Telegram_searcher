from databases.sqlite import sqlite3_client

import asyncio
import logging

logger = logging.getLogger()


async def wait_the_delete(url: str):
    logger.info(f'Начало проверки на занятость поля сообщения url - {url}')
    while True:
        message = sqlite3_client.get_message(url)
        if message != '':
            await asyncio.sleep(1)
        else:
            break