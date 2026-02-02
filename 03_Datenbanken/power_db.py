from database import Database
from models import Power


class PowerDB:
    def __init__(self, db: Database):
        self.db = db
    def power_exists(self, power_name: str) -> bool: 
        self.db.execute(
            "SELECT power_id FROM powers WHERE power = ?", 
            (power_name,)
        )
        return self.db.fetchone() is not None

    def power_exists_in_member(self, power_name: str, member_id: int) -> bool:
        self.db.execute(
            "SELECT member_id FROM powers WHERE power = ? AND member_id = ?",
            (power_name, member_id)
        )
        return self.db.fetchone() is not None


    def add_power(self, power: Power, member_id: int) -> None:
        if self.power_exists_in_member(power.power_name, member_id):
            return False
        self.db.execute(
            "INSERT INTO powers (power, member_id) VALUES (?, ?)",
            (
                power.power_name,
                member_id
            )
        )

        self.db.commit()

    def get_all_powers_by_member(self, member_id: int):
        self.db.execute(
            "SELECT power FROM powers WHERE member_id = ?",
            (member_id,)
        )
        return self.db.fetchall()