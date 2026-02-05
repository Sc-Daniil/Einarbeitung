from app import App
from database import Database
from squad_db import SquadDB
from member_db import MemberDB
from power_db import PowerDB
from parser import Parser
from ui import UI


PATH: str = "../base.json"

def main():
    db = Database("base.db")
    squad_db = SquadDB(db)
    member_db = MemberDB(db)
    power_db = PowerDB(db)
    app = App(UI(), SquadDB(db), MemberDB(db), PowerDB(db))
    

    db.try_make_tables()

    # JSON 
    data = Parser.get_data_from_file(PATH)
    squads = Parser.parse_squads(data)
    members = Parser.parse_members(data)
    powers = Parser.parse_powers(data)

    # ADD DATA TO DATENBANK
    for squad in squads:
        if not squad_db.squad_exists(squad.squad_name):
            squad_db.add_squad(squad)

    for member in members:
        if not member_db.member_exists(member.member_name):
            squad_id = squad_db.get_squad_id_by_name(member.squad_name)
            member_db.add_member(member, squad_id)

    for power in powers:
        if not power_db.power_exists(power.power_name):
            member_id = member_db.get_member_id_by_name(power.member_name) 
            power_db.add_power(power, member_id)

    app.run()

    db.close()

if __name__ == "__main__":
    main()