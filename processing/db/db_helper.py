from psycopg2 import pool
from psycopg2.extras import RealDictCursor
from contextlib import contextmanager
import atexit


class DBHelper:
    def __init__(self):
        self._connection_pool = None

    def initialize_connection_pool(self):
        db_dsn = 'postgresql://postgres:postgres@10.199.196.93:31656/k8s?connect_timeout=5'
        self._connection_pool = pool.ThreadedConnectionPool(1, 3, db_dsn)

    @contextmanager
    def get_resource(self, autocommit=True):
        if self._connection_pool is None:
            self.initialize_connection_pool()

        conn = self._connection_pool.getconn()
        conn.autocommit = autocommit
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        try:
            yield cursor, conn
        finally:
            cursor.close()
            self._connection_pool.putconn(conn)

    def shutdown_connection_pool(self):
        if self._connection_pool is not None:
            self._connection_pool.closeall()


db_helper = DBHelper()


@atexit.register
def shutdown_connection_pool():
    db_helper.shutdown_connection_pool()
