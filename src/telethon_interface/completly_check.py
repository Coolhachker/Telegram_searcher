from telethon import TelegramClient
from telethon.types import Chat
import asyncio

from src.json_buffer.Json_engine import JsonEngine
from src.telethon_interface.check_message import check_message
from src.telethon_interface.real_time_processing import realtime_processing


async def complete_check(url: str, client: TelegramClient):
    while True:
        json_data = JsonEngine.read()
        data_of_chat = json_data[url]
        message = await client.get_messages(url, offset_id=data_of_chat['id'], limit=1)
        print(message)
        data_of_chat['id'] = message[0].id
        try:
            if check_message(message[0].message):
                data_of_chat['id'] = message[0].id
                while data_of_chat['message'] != '':
                    await asyncio.sleep(.5)

                entity = await client.get_entity(message[0].peer_id.channel_id)
                print(entity)
                data_of_chat['message'] = f"Сообщение - {message[0].message}\nИз чата - {url}\n"
                if isinstance(entity, Chat) is False:
                    data_of_chat['message'] += f"Ссылка на сообщение - {url}/{message[0].id}"
                else:
                    data_of_chat["message"] += f"Ссылка на сообщение - https://t.me/c/{message[0].peer_id.channel_id}/{message[0].id}"
        except TypeError:
            data_of_chat['check_completely'] = 1
            json_data[url] = data_of_chat
            JsonEngine.write(json_data)

            await realtime_processing(url, client)

        json_data[url] = data_of_chat
        JsonEngine.write(json_data)

        await asyncio.sleep(.3)