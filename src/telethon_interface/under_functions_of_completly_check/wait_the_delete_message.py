import time

from src.json_buffer.Json_engine import JsonEngine

import asyncio
import logging

logger = logging.getLogger()


def wait_the_delete(url: str):
    logger.info(f'Начало проверки на занятость поля сообщения url - {url}')
    while True:
        json_data = JsonEngine.read()
        data_of_chat = json_data[url]
        if data_of_chat['message'] != '':
            time.sleep(1)
        else:
            break