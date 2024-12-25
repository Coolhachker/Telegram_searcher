from sqlite3 import Cursor, connect


class SQLite3Client:
    def __init__(self):
        self.connection, self.cursor = self.connect()

    @staticmethod
    def connect():
        connection = connect('tg')
        return connection, connection.cursor()


sqlite3_client = SQLite3Client()