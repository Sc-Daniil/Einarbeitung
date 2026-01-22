from database import Database
from models import Member


class MemberDB:
    def __init__(self, db: Database):
        self.db = db

    def member_exists(self, name: str) -> bool:
        self.db.execute(
            "SELECT member_id FROM members WHERE name = ?",
            (name,)
        )
        return self.db.fetchone() is not None

    def add_member(self, member: Member, squad_id: int) -> bool:
        if self.member_exists(member.member_name):
            return False

        self.db.execute(
            "INSERT INTO members (name, age, squad_id, secret_identity) VALUES (?, ?, ?, ?)",
            (
                member.member_name,
                member.age,
                squad_id,
                member.secret_identity
            )
        )

        self.db.commit()

        return True

    def get_by_squad(self, squad_id: int):
        self.db.execute(
            "SELECT * FROM members WHERE squad_id = ?",
            (squad_id,)
        )
        return self.db.fetchall()
    
    def get_member_id_by_name(self, member_name: str):
        self.db.execute(
            "SELECT member_id FROM members WHERE name = ?",
            (member_name,)
        )

        row = self.db.fetchone()
        if row:
            return row[0]
        return None