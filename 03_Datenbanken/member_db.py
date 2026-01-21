from database import Database


class MemberDB:
    def __init__(self, db: Database):
        self.db = db

    def add_member(self, squad_id: int, name: str, age: int, secret_id: str):
        self.db.execute(
            "INSERT INTO members (name, age, squad_id, secret_identity) VALUES (?, ?, ?, ?)",
            (name, age, squad_id, secret_id)
        )
        self.db.commit()

    def get_by_squad(self, squad_id: int):
        self.db.execute(
            "SELECT * FROM members WHERE squad_id = ?",
            (squad_id,)
        )
        return self.db.fetchall()
