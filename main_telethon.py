from src.telethon_interface.telethon_engine import TelethonEngine
import asyncio


if __name__ == '__main__':
    telethon_engine = TelethonEngine()
    asyncio.run(telethon_engine.run())

