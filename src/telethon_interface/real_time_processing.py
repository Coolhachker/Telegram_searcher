from telethon import TelegramClient
from telethon.types import User
import asyncio

from src.json_buffer.Json_engine import JsonEngine
from src.telethon_interface.check_message import check_message

from databases.sqlite import sqlite3_client


async def realtime_processing(url: str, client: TelegramClient):
    while True:
        json_data = JsonEngine.read()
        data_of_chat = json_data[url]
        ban_list = sqlite3_client.get_ban_members()

        message = await client.get_messages(url, limit=1)
        id_of_user = message[0].from_id.user_id
        entity_of_user = await client.get_entity(id_of_user)
        entity_of_user = '' if not isinstance(entity_of_user, User) else entity_of_user

        if check_message(message[0].message) and entity_of_user.username not in ban_list:
            while data_of_chat['message'] != '':
                await asyncio.sleep(.5)
            data_of_chat['message'] = f"""Сообщение - {message[0].message}\nИз чата - {url}\n"""
            data_of_chat["message"] += f"Ссылка на сообщение - https://t.me/c/{message[0].peer_id.channel_id}/{message[0].id}"
            json_data[url] = data_of_chat
            JsonEngine.write(url, json_data[url])

        await asyncio.sleep(5)
