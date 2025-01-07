import re
from databases.sqlite import sqlite3_client


def check_message(text: str):
    try:
        key_words = sqlite3_client.get_key_words()
        for key_word in key_words:
            if len(re.findall(key_word[0].lower(), text.lower().replace('\n', ' ').strip())) > 0:
                return True
        return False
    except Exception:
        return False
