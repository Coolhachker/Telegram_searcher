# import logging

from src.telethon_interface.telethon_engine import TelethonEngine
from databases.sqlite import sqlite3_client
# from logging import basicConfig
import asyncio

# basicConfig(filename='log.log', filemode='w', level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")


if __name__ == '__main__':
    telethon_engine = TelethonEngine()
    telethon_engine.client.start()
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(telethon_engine.run())
    sqlite3_client.add_pid(0)