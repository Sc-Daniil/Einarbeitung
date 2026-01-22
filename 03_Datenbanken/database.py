import sqlite3

class Database:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cur = self.connection.cursor()

    def make_tables(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS powers (
                    power_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    power TEXT,
                    member_id INTEGER,
                    FOREIGN KEY(member_id) REFERENCES members(member_id)) 
        """)

        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS members (
                member_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                squad_id INTEGER,
                secret_identity TEXT,
                FOREIGN KEY(squad_id) REFERENCES squads(squad_id)   
                
            )
        """)

        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS squads (
                squad_id INTEGER PRIMARY KEY AUTOINCREMENT,
                squad_name TEXT,
                home_town TEXT,
                formed INTEGER,
                status TEXT,
                secret_base TEXT,
                active BOOLEAN
            )
        """)

        self.connection.commit() 
    def execute(self, sql: str, params: tuple = ()):
        self.cur.execute(sql, params)

    def fetchone(self):
        return self.cur.fetchone()

    def fetchall(self):
        return self.cur.fetchall()

    def lastrowid(self) -> int:
        return self.cur.lastrowid

    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()
