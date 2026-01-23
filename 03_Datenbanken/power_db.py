from database import Database
from models import Power


class PowerDB:
    def __init__(self, db: Database):
        self.db = db

    def power_exists(self, power_name: str) -> bool:
        self.db.execute(
            "SELECT 1 FROM powers WHERE power = ?",
            (power_name,)
        )
        return self.db.fetchone() is not None


    def add_power(self, power: Power, member_id: int) -> None:
        if self.power_exists(power.power_name):
            return False
        self.db.execute(
            "INSERT INTO powers (power, member_id) VALUES (?, ?)",
            (
                power.power_name,
                member_id
            )
        )

        self.db.commit()

    def get_by_member(self, member_id: int):
        self.db.execute(
            "SELECT * FROM powers WHERE member_id = ?",
            (member_id,)
        )
        return self.db.fetchall()
