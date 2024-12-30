import asyncio
from asyncio.tasks import Task
from telethon import TelegramClient

from databases.sqlite import sqlite3_client
from src.json_buffer.Json_engine import JsonEngine
from src.telethon_interface.completly_check import complete_check
from src.telethon_interface.real_time_processing import realtime_processing

import os


class TelethonEngine:
    def __init__(self):
        self.client = TelegramClient(api_id=19567654, api_hash='7ec7d44a4889e041dd667dc760b323e1', session='session.session', system_version="4.16.30-vxCUSTOM")
        pid = os.getpid()
        sqlite3_client.add_pid(pid)
        JsonEngine.setup_json_structure()

    async def run(self):
        await self.center_run_tasks()

    async def center_run_tasks(self):
        tasks = self.central_processing_of_registration_tasks()
        await asyncio.gather(*tasks, return_exceptions=True)

    def central_processing_of_registration_tasks(self):
        list_of_chats = sqlite3_client.get_chats()
        list_of_tasks: list[Task] = []

        for chat in list_of_chats:
            list_of_tasks.append(asyncio.create_task(self.center_of_processing_task(chat[2]), name=chat[2]))

        return list_of_tasks

    async def center_of_processing_task(self, url: str):
        json_data = JsonEngine.read()
        data_of_chat = json_data[url]
        if data_of_chat['check_completely'] == 0:
            await complete_check(url, self.client)
        else:
            await realtime_processing(url, self.client)



