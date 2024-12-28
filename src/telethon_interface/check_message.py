import re
from databases.sqlite import sqlite3_client


def check_message(text: str):
    try:
        key_words = sqlite3_client.get_key_words()
        for key_word in key_words:
            if re.findall(key_word[0], text.lower().replace('\n', ' ').strip()):
                return True
        return False
    except Exception:
        return False
