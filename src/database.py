import psycopg2

class Database:
    def __init__(self, dbname, user, password, host='localhost', port='5432'):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.connection.cursor()
            print("Ура")
        except Exception as e:
            print(f"Ошибка: {e}")
            self.cursor = None
        return self.connection

    def create_tables(self):
        if self.cursor is None:
            print("присоединитесь к базе данных")
            return

        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS dishes (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    calories INTEGER NOT NULL,
                    proteins INTEGER NOT NULL,
                    fats INTEGER NOT NULL,
                    carbs INTEGER NOT NULL
                )
            ''')
            self.connection.commit()
        except Exception as e:
            print(f"таблица упала((: {e}")

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()