from models import Squad
from database import Database

class SquadDB:
    ALLOWED_COLUMNS = {"squad_id", "squad_name", "home_town", "formed", "status", "secret_base", "active"}

    def __init__(self, db: Database):
        self.db = db

    def squad_exists(self, squad_name: str) -> bool:
        self.db.execute(
            "SELECT 1 FROM squads WHERE squad_name = ? LIMIT 1",
            (squad_name,)
        )
        return self.db.fetchone() is not None

    def add_squad(self, squad: Squad) -> None:
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

    def get_squad_id_by_name(self, squad_name: str):
        self.db.execute(
            "SELECT squad_id FROM squads WHERE squad_name = ?",
            (squad_name,)
        )

        row = self.db.fetchone()
        if row is None:
            return None

        return row[0]
    
    def get_all_squads_names(self):
        self.db.execute(
            "SELECT squad_name FROM squads"
        )

        rows = self.db.fetchall()

        if not rows:
            return []

        return rows
    
    def get_all_squads_info(self):
        self.db.execute(
            "SELECT * FROM squads"
        )

        rows = self.db.fetchall()

        if not rows:
            return []

        return rows

    def remove_squad(self, squad_id: int) -> None:
        self.db.execute(
            "DELETE FROM squads WHERE squad_id = ?", 
            (squad_id,)
        )

        self.db.commit()

    def update_squad_value(self, new_value, column: str, squad_id: int) -> None:
        if column not in self.ALLOWED_COLUMNS:
            raise ValueError("Invalid column name in squad_db.py")

        self.db.execute(
            f"UPDATE squads SET {column} = ? WHERE squad_id = ?",
            (new_value, squad_id,)
        )

        self.db.commit()