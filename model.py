import psycopg2


class Model:
    def __init__(self):
        self.cursor = None
        self.connectionDataBase = None

    def connection_database(self):
        self.connectionDataBase = psycopg2.connect(dbname='niva1', user='postgres',
                                                   password='root', host='127.0.0.1')
        self.cursor = self.connectionDataBase.cursor()
        self.connectionDataBase.autocommit = True
        # self.select_niva_db()

    def send_request_to_db(self, request):

        self.cursor.execute(request)

    def select_niva_db(self):
        self.send_request_to_db("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'niva1'")

    def create_table_credential_if_not_exist(self):
        self.send_request_to_db("CREATE TABLE IF NOT EXISTS credential (id SERIAL PRIMARY KEY, "
                                "login text,  password text)")

    def select_from_credential(self):
        self.send_request_to_db("SELECT * FROM credential")

    def get_count_of_users(self):
        self.select_from_credential()
        return self.cursor.fetchall()
