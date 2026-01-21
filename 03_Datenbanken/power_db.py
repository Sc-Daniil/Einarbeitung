from database import Database


class PowerDB:
    def __init__(self, db: Database):
        self.db = db

    def get_by_member(self, member_id: int):
        self.db.execute(
            "SELECT power FROM powers WHERE member_id = ?",
            (member_id,)
        )
        return self.db.fetchall()
