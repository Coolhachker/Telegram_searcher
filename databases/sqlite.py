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
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS pid_table(pid INT UNSIGNED)""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS admin_chats(chat_id INT, PRIMARY KEY(chat_id))""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS ban_users(nickname TEXT, id INT, PRIMARY KEY(nickname))""")

        self.connection.commit()

        self.cursor.execute("""SELECT * FROM pid_table""")
        if len(self.cursor.fetchall()) == 0:
            self.cursor.execute("""INSERT INTO pid_table(pid) VALUES(?)""", (None,))

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

    def get_pid(self):
        self.cursor.execute("""SELECT * FROM pid_table""")
        pid = self.cursor.fetchall()

        if len(pid) != 0:
            return pid[0][0]
        else:
            return None

    def add_pid(self, pid: int):
        self.cursor.execute(f"""UPDATE pid_table SET pid = {pid}""")

        self.connection.commit()

    def add_admin_chat(self, chat_id: int):
        self.cursor.execute("""INSERT INTO admin_chats(chat_id) VALUES(?)""", (chat_id, ))
        self.connection.commit()

    def get_admin_chats(self):
        self.cursor.execute("""SELECT * FROM admin_chats""")
        return self.cursor.fetchall()

    def add_ban_member_into_table(self, nickname: str):
        self.cursor.execute("""INSERT INTO ban_users(nickname) VALUES(?)""", (nickname, ))
        self.connection.commit()

    def delete_ban_member_from_table(self, nickname: str):
        self.cursor.execute(f"""DELETE FROM ban_users WHERE nickname = "{nickname}" """)
        self.connection.commit()

    def get_ban_members(self) -> list[str]:
        self.cursor.execute("""SELECT nickname FROM ban_users""")
        return [user[0] for user in self.cursor.fetchall()]


sqlite3_client = SQLite3Client()