import json
from databases.sqlite import sqlite3_client


class JsonEngine:
    @staticmethod
    def write(data: dict[str, dict]):
        with open('data.json', "r", encoding='utf-8') as file:
            json_data = json.load(file)
            for key, value in data.items():
                json_data[key] = value
        with open('data.json', 'w', encoding='utf-8') as file:
            json.dump(json_data, file, indent=4, ensure_ascii=False)

    @staticmethod
    def read():
        with open('data.json', 'r', encoding='utf-8') as file:
            json_data = json.load(file)
            return json_data

    @staticmethod
    def setup_json_structure():
        urls = sqlite3_client.get_chats()
        dict_of_urls: dict = {}

        urls_from_file = JsonEngine.read()
        dict_of_urls = urls_from_file if len(urls_from_file) != 0 else dict_of_urls

        urls_from_file_keys = urls_from_file.keys()

        for url in urls:
            if url[2] not in urls_from_file_keys:
                dict_of_urls[url[2]] = {
                    'id': 0,
                    'message': '',
                    'check_completely': 0
                }
        with open('data.json', 'w', encoding='utf-8') as file:
            json.dump(dict_of_urls, file, indent=4, ensure_ascii=False)




