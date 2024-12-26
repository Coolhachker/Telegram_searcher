import asyncio
from asyncio.tasks import Task
from telethon import TelegramClient

from databases.sqlite import sqlite3_client
from src.json_buffer.Json_engine import JsonEngine
from src.telethon_interface.check_message import check_message


class TelethonEngine:
    def __init__(self):
        self.client = TelegramClient(api_id=19567654, api_hash='7ec7d44a4889e041dd667dc760b323e1', session='session.session')

    async def run(self):
        await self.center_run_tasks()

    async def center_run_tasks(self):
        tasks = self.central_processing_of_registration_tasks()
        await asyncio.gather(tasks)

    async def central_processing_of_registration_tasks(self):
        list_of_chats = sqlite3_client.get_chats()
        list_of_tasks: list[Task] = []

        for chat in list_of_chats:
            list_of_tasks.append(asyncio.create_task(self.center_of_processing_task(chat[2]), name=chat[2]))

        return list_of_tasks

    async def center_of_processing_task(self, url: str):
        while True:
            json_data = JsonEngine.read()
            data_of_chat = json_data[url]

            message = await self.client.get_messages(url, offset_id=data_of_chat['id'], limit=1)
            if check_message(message[0].message):
                data_of_chat['id'] = message[0].id
                while data_of_chat['message'] == '':
                    await asyncio.sleep(.5)
                data_of_chat['message'] = f"""Сообщение - {message[0].message}\nИз чата - {url}"""

            await asyncio.sleep(.5)



