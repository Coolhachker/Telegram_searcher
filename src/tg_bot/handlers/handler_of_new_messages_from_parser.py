import asyncio
from aiogram import Bot

from src.json_buffer.Json_engine import JsonEngine
from databases.sqlite import sqlite3_client

from src.tg_bot.handlers.under_functions_of_handler_of_new_messages_from_parser.send_message_into_admin_chats import send_messages_into_admin_chats


async def handle_new_messages_from_parser(bot: Bot):
    while True:
        urls = sqlite3_client.get_chats()
        admin_chats = sqlite3_client.get_admin_chats()
        try:
            json_data = JsonEngine.read()
            for url in urls:
                try:
                    data = json_data[url[2]]
                    if data['message'] != '':
                        await send_messages_into_admin_chats(data['message'], admin_chats, bot)
                        data['message'] = ''
                        json_data[url[2]] = data
                        JsonEngine.write(json_data)
                    await asyncio.sleep(.3)
                except KeyError:
                    continue
        except FileNotFoundError:
            pass
        await asyncio.sleep(.3)