from database import Database
from models import Power


class PowerDB:
    def __init__(self, db: Database):
        self.db = db

    def power_exists(self, power_name: str) -> bool: 
        self.db.execute(
            "SELECT 1 FROM powers WHERE power_name = ? LIMIT 1", 
            (power_name,)
        )
        
        row = self.db.fetchone()
        if row is None:
            return None

        return row[0]

    def power_exists_in_member(self, power_name: str, member_id: int) -> bool:
        self.db.execute(
            "SELECT member_id FROM powers WHERE power_name = ? AND member_id = ?",
            (power_name, member_id)
        )

        row = self.db.fetchone()
        if row is None:
            return None

        return row[0]


    def add_power(self, power_name: Power, member_id: int) -> None:
        if self.power_exists_in_member(power_name.power_name, member_id):
            return False

        self.db.execute(
            "INSERT INTO powers (power_name, member_id) VALUES (?, ?)",
            (
                power_name.power_name,
                member_id
            )
        )

        self.db.commit()

    def get_power_id_by_name_in_member(self, power_name: str, member_id: int):
        self.db.execute(
            "SELECT power_name FROM powers WHERE power_name = ? AND member_id = ?",
            (power_name, member_id,)
        )

        row = self.db.fetchone()
        if row is None:
            return None

        return row[0]

    def get_power_id_by_member_id(self, member_id: int):
        self.db.execute(
            "SELECT power_id FROM powers WHERE member_id = ?",
            (member_id,)
        )
        return self.db.fetchall()

    def get_power_id_by_name(self, power_name: str):
        self.db.execute(
            "SELECT power_id FROM powers WHERE power_name = ?",
            (power_name,)
        )

        row = self.db.fetchone()
        if row is None:
            return None

        return row[0]

    def get_all_powers_by_member(self, member_id: int) -> list:
        self.db.execute(
            "SELECT power_name FROM powers WHERE member_id = ?",
            (member_id,)
        )
        rows = self.db.fetchall()
        if not rows:
            return []
        return rows


    def remove_power(self, power_id: int) -> None:
        self.db.execute(
            "DELETE FROM powers WHERE power_id = ?", 
            (power_id,)
        )

        self.db.commit()

    def update_power_name(self, new_power_name, power_id: int) -> None:
        self.db.execute(
            "UPDATE powers SET power_name = ? WHERE power_id = ?",
            (new_power_name, power_id,)
        )
        
        self.db.commit()

