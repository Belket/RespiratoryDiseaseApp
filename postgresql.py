import psycopg2
from contextlib import closing
from psycopg2.extras import DictCursor


class Postgres:

    def __ini__(self, database_name, user, password, host):
        self.database_name = database_name
        self.database_user = user
        self.database_password = password
        self.database_host = host

    def db_request(self, sql_request):
        with closing(psycopg2.connect(dbname=self.database_name, user=self.database_user, password=self.database_user, host=self.database_host)) as connection:
            with connection.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute(sql_request)
                response = cursor.fetchall()
        return response
