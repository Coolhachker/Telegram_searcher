from sqlite3 import Cursor, connect


class SQLite3Client:
    def __init__(self):
        self.connection, self.cursor = self.connect()
        self.create_table()

    @staticmethod
    def connect():
        connection = connect('tg.sql')
        return connection, connection.cursor()

    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS chats(id LONG INT, name_of_chat TEXT, url TEXT, PRIMARY KEY(url))""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS key_words(word TEXT, PRIMARY KEY(word))""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS pid_table(pid INT UNSIGNED, PRIMARY KEY(pid))""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS admin_chats(chat_id INT, PRIMARY KEY(chat_id))""")
        self.connection.commit()

    def add_chat_into_table(self, url: str):
        self.cursor.execute("""INSERT INTO chats(url) VALUES(?)""", (url, ))
        self.connection.commit()

    def delete_chat_from_table(self, url: str):
        self.cursor.execute(f"""DELETE FROM chats WHERE url = "{url}" """)
        self.connection.commit()

    def get_chats(self):
        self.cursor.execute("""SELECT * FROM chats""")
        return self.cursor.fetchall()

    def add_data_into_entry(self, chat_id: int, data: dict):
        arguments = [f'{key}={value}' for key, value in data.items()]
        arguments = ', '.join(arguments)

        self.cursor.execute(f"""UPDATE chats SET {arguments} WHERE id = {chat_id}""")

    def add_key_word(self, word: str):
        self.cursor.execute("""INSERT INTO key_words(word) VALUES(?)""", (word, ))
        self.connection.commit()

    def delete_key_word(self, word: str):
        self.cursor.execute(f"""DELETE FROM key_words WHERE word = "{word}" """)
        self.connection.commit()

    def get_key_words(self):
        self.cursor.execute("""SELECT * FROM key_words""")
        return self.cursor.fetchall()

    def update_key_word(self, key_word: str, new_key_word: str):
        self.cursor.execute(f"""UPDATE key_words SET word = "{new_key_word}" WHERE word = "{key_word}" """)
        self.connection.commit()

    def add_pid(self, pid: int):
        try:
            self.cursor.execute("""INSERT INTO pid_table(pid) VALUES(?)""", (pid, ))
        except:
            self.cursor.execute(f"""UPDATE pid_table SET pid = {pid}""")

        self.connection.commit()

    def add_admin_chat(self, chat_id: int):
        self.cursor.execute("""INSERT INTO admin_chats(chat_id) VALUES(?)""", (chat_id, ))
        self.connection.commit()


sqlite3_client = SQLite3Client()