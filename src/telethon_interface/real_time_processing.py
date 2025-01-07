import re
from telethon import TelegramClient
from telethon.types import User
import asyncio

from src.telethon_interface.check_message import check_message

from databases.sqlite import sqlite3_client


async def realtime_processing(url: str, client: TelegramClient):
    while True:
        ban_list = sqlite3_client.get_ban_members()
        admins_chats = [chat[0] for chat in sqlite3_client.get_admin_chats()]

        messages_in_admin_chats: list[str] = []

        for admin_chat in admins_chats:
            messages = await client.get_messages(admin_chat, limit=30)
            for message in messages:
                if isinstance(message.message, str):
                    match = re.findall('(\d+)/(\d+)', message.message)
                    if len(match) != 0:
                        messages_in_admin_chats.append(match[0][0]+'/'+match[0][1])
            await asyncio.sleep(.3)

        message = await client.get_messages(url, limit=1)
        id_of_user = message[0].from_id.user_id
        entity_of_user = await client.get_entity(id_of_user)
        entity_of_user = '' if not isinstance(entity_of_user, User) else entity_of_user

        if check_message(message[0].message) and entity_of_user.username not in ban_list and (str(message[0].peer_id.channel_id)+"/"+str(message[0].id)) not in messages_in_admin_chats:
            message_text = f"""Сообщение - {message[0].message}\nИз чата - {url}\n"""
            message_text += f"""Ссылка на сообщение - https://t.me/c/{message[0].peer_id.channel_id}/{message[0].id}"""

            sqlite3_client.update_message(url, message_text)

        await asyncio.sleep(5)
