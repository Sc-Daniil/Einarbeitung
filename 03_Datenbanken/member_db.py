from database import Database
from models import Member

class MemberDB:
    def __init__(self, db: Database):
        self.db = db

    def member_exists(self, member_name: str) -> bool:
        self.db.execute(
            "SELECT 1 FROM members WHERE member_name = ? LIMIT 1",
            (member_name,)
        )

        row = self.db.fetchone()

        if row is None:
            return None

        return row[0]

    def member_exists_in_squad(self, member_name, squad_id):
        self.db.execute(
            "SELECT member_name FROM members WHERE member_name = ? AND squad_id = ?",
            (member_name, squad_id,)
        )

        row = self.db.fetchone()

        if row is None:
            return None

        return row[0]

    def add_member(self, member: Member, squad_id: int) -> None:
        self.db.execute(
            "INSERT INTO members (member_name, member_age, squad_id, secret_identity) VALUES (?, ?, ?, ?)",
            (
                member.member_name,
                member.member_age,
                squad_id,
                member.secret_identity
            )
        )

        self.db.commit()

    def remove_member(self, member_id: int) -> None:
        self.db.execute(
            "DELETE FROM members WHERE member_id = ?",
            (member_id,)
        )

        self.db.commit()


    def get_member_by_squad(self, squad_id: int):
        self.db.execute(
            "SELECT * FROM members WHERE squad_id = ?",
            (squad_id,)
        )

        rows = self.db.fetchall()

        if not rows:
            return []

        return rows
    
    def get_member_id_by_name(self, member_name: str):
        self.db.execute(
            "SELECT member_id FROM members WHERE member_name = ?",
            (member_name,)
        )

        row = self.db.fetchone()
        if row is None:
            return None

        return row[0]


    def get_member_id_by_member_name_in_squad(self, member_name: str, squad_id: int):
        self.db.execute(
            "SELECT member_id FROM members WHERE member_name = ? AND squad_id = ?",
            (member_name, squad_id,)
        )

        row = self.db.fetchone()

        if row is None:
            return None

        return row[0]

    def get_all_member_names_in_squad(self, squad_id: int):
        self.db.execute(
            "SELECT member_name FROM members WHERE squad_id = ?",
            (squad_id,)
        )
        
        rows = self.db.fetchall()
        if not rows:
            return []

        return rows

    def get_all_members_by_squad(self, squad_id: int):
        self.db.execute(
            "SELECT * FROM members WHERE squad_id = ?",
            (squad_id,)
        )

        rows = self.db.fetchall()
        if not rows:
            return []

        return rows