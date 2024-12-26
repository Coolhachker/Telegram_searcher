from telethon import TelegramClient
import asyncio

from src.json_buffer.Json_engine import JsonEngine
from src.telethon_interface.check_message import check_message
from src.telethon_interface.real_time_processing import realtime_processing


async def complete_check(url: str, client: TelegramClient):
    try:
        while True:
            json_data = JsonEngine.read()
            data_of_chat = json_data[url]

            message = await client.get_messages(url, offset_id=data_of_chat['id'], limit=1)
            if check_message(message[0].message):
                data_of_chat['id'] = message[0].id
                while data_of_chat['message'] == '':
                    await asyncio.sleep(.5)
                data_of_chat['message'] = f"""Сообщение - {message[0].message}\nИз чата - {url}"""
                JsonEngine.write(data_of_chat)

            await asyncio.sleep(.3)
    except:
        json_data = JsonEngine.read()
        data_of_chat = json_data[url]
        data_of_chat['check_completely'] = 1
        JsonEngine.write(data_of_chat)

        await realtime_processing(url, client)