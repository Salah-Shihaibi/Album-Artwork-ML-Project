import psycopg2
from psycopg2.extras import RealDictCursor


def connect():
    connection = psycopg2.connect(
        user="postgres",
        password="0",
        host="127.0.0.1",
        port="5432",
        database="album_cover_db",
        cursor_factory=RealDictCursor,
    )
    return connection
