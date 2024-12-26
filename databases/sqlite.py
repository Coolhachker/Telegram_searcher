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


sqlite3_client = SQLite3Client()