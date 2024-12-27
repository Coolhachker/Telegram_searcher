from telethon import TelegramClient
import asyncio

from src.json_buffer.Json_engine import JsonEngine
from src.telethon_interface.check_message import check_message


async def realtime_processing(url: str, client: TelegramClient):
    while True:
        json_data = JsonEngine.read()
        data_of_chat = json_data[url]

        message = await client.get_messages(url, limit=1)
        print(message)
        if check_message(message[0].message):
            while data_of_chat['message'] != '':
                await asyncio.sleep(.5)
            data_of_chat['message'] = f"""Сообщение - {message[0].message}\nИз чата - {url}"""
            data_of_chat["message"] += f"Ссылка на сообщение - https://t.me/c/{message[0].peer_id.channel_id}/{message[0].id}"
            json_data[url] = data_of_chat
            JsonEngine.write(json_data)

        await asyncio.sleep(.5)
