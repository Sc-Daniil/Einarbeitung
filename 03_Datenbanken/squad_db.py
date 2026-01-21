from models import Squad
from database import Database

class SquadDB:
    def __init__(self, db: Database):
        self.db = db

    def squad_exists(self, name: str) -> bool:
        self.db.execute(
            "SELECT squad_id FROM squads WHERE squad_name = ?",
            (name,)
        )
        return self.db.fetchone() is not None

    def add_squad(self, squad: Squad) -> bool:
        if self.squad_exists(squad.squad_name):
            return False

        self.db.execute(
            """
            INSERT INTO squads
            (squad_name, home_town, formed, status, secret_base, active)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                squad.squad_name,
                squad.home_town,
                squad.formed,
                squad.status,
                squad.secret_base,
                squad.active
            )
        )
        self.db.commit()
        return True
