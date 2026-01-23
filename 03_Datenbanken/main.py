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
    ui = UI()

    db.make_tables()

    data = Parser.get_data_from_file(PATH)
    squads = Parser.parse_squads(data)
    members = Parser.parse_members(data)
    powers = Parser.parse_powers(data)

    for squad in squads:
        squad_db.add_squad(squad)
    
    for member in members:
        squad_id = squad_db.get_squad_id_by_name(member.squad_name)
        member_db.add_member(member, squad_id)

    for power in powers:
        member_id = member_db.get_member_id_by_name(power.member_name) 
        power_db.add_power(power, member_id)

    while True:
        choice = ui.main_menu()

        if choice == "1":
            sub = ui.show_menu()

            if sub == "1":
                pass  

            elif sub == "2":
                pass 

            elif sub == "3":
                pass 

            elif sub == "4" or sub.lower() == "b":
                continue

            elif sub == "5" or sub.lower() == "x":
                break

        elif choice == "2":
            sub = ui.add_menu()

            if sub == "1":
                squad_name = ui.get_squad_name()
                if not squad_db.squad_exists(squad_name):
                    squad = ui.create_squad(squad_name)
                    squad_db.add_squad(squad)
                    print(f"New Squad {squad_name} was added.")
                else:
                    print("Squad already exists.")

            elif sub == "2":
                input_member_name = ui.get_member_name()
                if not member_db.member_exists(input_member_name):
                    print("To which squad do you want to add a member?")
                    input_squad_name = ui.get_squad_name()
                    squad_name_to_squad_id = squad_db.get_squad_id_by_name(input_squad_name)
                    new_member = ui.create_member(input_member_name, input_squad_name) 
                    member_db.add_member(new_member, squad_name_to_squad_id)
                    print(f"New Member {input_member_name} was added to {input_squad_name}.")
                else: 
                    print("Member already exists.")

            elif sub == "3":
                input_power_name = ui.get_power_name()
                if not power_db.power_exists(input_power_name):
                    print("To which member do you want to add power?")
                    input_member_name = ui.get_member_name()
                    member_name_to_member_id = member_db.get_member_id_by_name(input_power_name)
                    new_power = ui.create_power(input_power_name, input_member_name)
                    power_db.add_power(new_power, member_name_to_member_id)
                    print(f"New Power {input_power_name} added to {input_member_name}.")
                else: 
                    print("Power already exists.")

            elif sub == "4" or sub.lower() == "b":
                continue

            elif sub == "5" or sub.lower() == "x":
                break

        elif choice == "3":
            pass  

        elif choice == "4":
            pass 

        elif choice == "5" or choice.lower() == "x":
            break

        else:
            print("\nIncorrect option. Try again.\n")

    db.close()


if __name__ == "__main__":
    main()
