import asyncio
import json.decoder
import time

from aiogram import Bot

from src.json_buffer.Json_engine import JsonEngine
from databases.sqlite import sqlite3_client

from src.tg_bot.handlers.under_functions_of_handler_of_new_messages_from_parser.send_message_into_admin_chats import send_messages_into_admin_chats


async def handle_new_messages_from_parser(bot: Bot):
    while True:
        urls = [url[2] for url in sqlite3_client.get_chats()]
        admin_chats = sqlite3_client.get_admin_chats()
        try:
            for url in urls:
                message = sqlite3_client.get_message(url)
                if message != '':
                    sqlite3_client.update_message(url, '')
                    await send_messages_into_admin_chats(message, admin_chats, bot)
        except (FileNotFoundError, TypeError, json.JSONDecodeError):
            pass
        await asyncio.sleep(.1)