from telethon import TelegramClient
from databases.sqlite import sqlite3_client


class TelethonEngine:
    def __init__(self):
        self.client = TelegramClient(api_id=19567654, api_hash='7ec7d44a4889e041dd667dc760b323e1', session='session')

    def check_messages(self):
        pass


