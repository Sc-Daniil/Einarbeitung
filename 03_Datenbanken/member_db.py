from database import Database
from models import Member

class MemberDB:
    def __init__(self, db: Database):
        self.db = db

    def member_exists(self, member_name: str) -> bool:
        self.db.execute(
            "SELECT member_id FROM members WHERE name = ?",
            (member_name,)
        )
        return self.db.fetchone() is not None

    def add_member(self, member: Member, squad_id: int) -> None:

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


    def get_member_by_squad(self, squad_id: int):
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
        return row[0] 


    def get_all_member_names_in_squad(self, squad_id: int):
        self.db.execute(
            "SELECT name FROM members WHERE squad_id = ?",
            (squad_id,)
        )
        
        return self.db.fetchall()

    def get_all_members_by_squad(self, squad_id: int):
        self.db.execute(
            "SELECT * FROM members WHERE squad_id = ?",
            (squad_id,)
        )

        return self.db.fetchall()