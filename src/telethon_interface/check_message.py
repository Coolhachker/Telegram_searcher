import re
from databases.sqlite import sqlite3_client


def check_message(text: str):
    key_words = sqlite3_client.get_key_words()
    for key_word in key_words:
        if re.search(key_word[0], text):
            return True
    return False
