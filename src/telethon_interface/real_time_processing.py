from telethon import TelegramClient
import asyncio

from src.json_buffer.Json_engine import JsonEngine
from src.telethon_interface.check_message import check_message


async def realtime_processing(url: str, client: TelegramClient):
    while True:
        json_data = JsonEngine.read()
        data_of_chat = json_data[url]

        message = await client.get_messages(url, limit=1)
        if check_message(message[0].message):
            while data_of_chat['message'] == '':
                await asyncio.sleep(.5)
            data_of_chat['message'] = f"""Сообщение - {message[0].message}\nИз чата - {url}"""
            JsonEngine.write(data_of_chat)

        await asyncio.sleep(.3)
