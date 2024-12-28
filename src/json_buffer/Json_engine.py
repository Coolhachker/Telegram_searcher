import json
from databases.sqlite import sqlite3_client
import logging
logger = logging.getLogger()


class JsonEngine:
    @staticmethod
    def write(key_url: str, data: dict):
        with open('data.json', "r", encoding='utf-8') as file:
            json_data = json.load(file)
            logger.info(f'Старые данные json_data = {json_data}')

            json_data[key_url] = data
            logger.info(f'Новые данные json_data = {json_data}')
        with open('data.json', 'w', encoding='utf-8') as file:
            file.write(json.dumps(json_data, indent=4, ensure_ascii=False))

    @staticmethod
    def read():
        try:
            with open('data.json', 'r', encoding='utf-8') as file:
                json_data = json.load(file)
                return json_data
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            with open('data.json', 'w', encoding='utf-8') as file:
                file.write(json.dumps({}, indent=4, ensure_ascii=False))

    @staticmethod
    def setup_json_structure():
        urls = [chat[2] for chat in sqlite3_client.get_chats()]
        dict_of_urls: dict = {}

        urls_from_file = JsonEngine.read()
        dict_of_urls = urls_from_file if len(urls_from_file) != 0 else dict_of_urls

        urls_from_file_keys = urls_from_file.keys()

        list_of_deleting_urls = [url for url in urls_from_file_keys if url not in urls]
        for deleting_url in list_of_deleting_urls:
            del dict_of_urls[deleting_url]

        for url in urls:
            if url not in urls_from_file_keys:
                dict_of_urls[url] = {
                    'id': 0,
                    'message': '',
                    'check_completely': 0
                }
        with open('data.json', 'w', encoding='utf-8') as file:
            json.dump(dict_of_urls, file, indent=4, ensure_ascii=False)




