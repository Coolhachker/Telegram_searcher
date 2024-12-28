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
                json_data = JsonEngine.read()
                try:
                    data = json_data[url]
                    if data['message'] != '':
                        print(json_data)
                        message = data['message']

                        data['message'] = ''
                        json_data[url] = data
                        JsonEngine.write(url, data)

                        await send_messages_into_admin_chats(message, admin_chats, bot)
                except KeyError:
                    continue
        except FileNotFoundError:
            pass
        except json.decoder.JSONDecodeError:
            pass
        await asyncio.sleep(.1)