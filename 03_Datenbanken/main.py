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

    # MAIN OPTIONS
    while True:
        choice = ui.main_menu()
        # SHOW OPTION
        if choice == "1":
            sub = ui.show_menu()

            # SHOW ALL
            if sub == "1":
                squads_info = squad_db.get_all_squads_info()
                for squad_info in squads_info:
                    ui.show_all_squads(squad_info)
                    squad_id = squad_info[0]
                    members_info = member_db.get_all_members_by_squad(squad_id)

                    if members_info is None:
                        continue

                    for member_info in members_info:
                        ui.show_all_members(member_info) 
                        member_id = member_info[0]
                        powers_info = power_db.get_all_powers_by_member(member_id)

                        if powers_info is None:
                            continue

                        for power_info in powers_info:
                            ui.show_all_powers(power_info)

            # SHOW SQUAD'S NAME
            elif sub == "2":
                squads_name = squad_db.get_all_squads_names()
                ui.show_squads_names(squads_name)

            # SHOW MEMBER'S NAMES
            elif sub == "3":
                input_squad_name = ui.get_squad_name()
                
                if not squad_db.squad_exists(input_squad_name):
                    print("Incorrect squad name.")

                squad_id = squad_db.get_squad_id_by_name(input_squad_name)
                members_names = member_db.get_all_member_names_in_squad(squad_id)

                ui.show_members_names(members_names)

            # SHOW POWERS
            elif sub == "4":
                input_member_name = ui.get_member_name()
                
                if not member_db.member_exists(input_member_name):
                    print("\nIncorrect member name.\n")
                    continue

                member_id = member_db.get_member_id_by_name(input_member_name)
                powers_names = power_db.get_all_powers_by_member(member_id)

                ui.show_powers_names(powers_names)

            elif sub == "5" or sub.lower() == "b":
                continue

            elif sub == "6" or sub.lower() == "x":
                break

        # ADD OPTION
        elif choice == "2":
            sub = ui.add_menu()

            # ADD SQUAD
            if sub == "1":
                squad_name = ui.get_squad_name()

                if squad_db.squad_exists(squad_name):
                    print("\nSquad already exists.\n")
                    continue

                squad = ui.create_squad(squad_name)

                squad_db.add_squad(squad)
                print(f"\nNew Squad {squad_name} was added.\n")

            # ADD MEMBER IN SQUAD
            elif sub == "2":
                input_member_name = ui.get_member_name()

                if member_db.member_exists(input_member_name):
                    print("\nMember already exists.\n")
                    continue

                print("\nTo which squad do you want to add a member?\n")
                input_squad_name = ui.get_squad_name()

                squad_name_to_squad_id = squad_db.get_squad_id_by_name(input_squad_name)

                new_member = ui.create_member(input_member_name, input_squad_name) 

                member_db.add_member(new_member, squad_name_to_squad_id)
                print(f"\nNew Member {input_member_name} was added to {input_squad_name}.\n")


            # ADD POWER IN MEMBER
            elif sub == "3":
                print("\nTo which member do you want to add power?\n")
                input_member_name = ui.get_member_name()

                if not member_db.member_exists(input_member_name):
                    print("\nMember doesn't exist.\n")
                    continue

                print(f"\nWrite power, which you want do add to {input_member_name}.\n")
                input_power_name = ui.get_power_name()

                if power_db.power_exists_in_member(input_power_name, member_id):
                    print(f"\nPower {input_power_name} already exists in member {input_member_name}\n")
                    continue

                member_name_to_member_id = member_db.get_member_id_by_name(input_power_name)
                new_power = ui.create_power(input_power_name, input_member_name)

                power_db.add_power(new_power, member_name_to_member_id)
                print(f"\nNew Power {input_power_name} added to {input_member_name}.\n")


            elif sub == "4" or sub.lower() == "b":
                continue

            elif sub == "5" or sub.lower() == "x":
                break

            else:
                print("\nIncorrect option. Try again.\n")

        # OVERWRITE OPTION
        elif choice == "3":
            sub = ui.overwrite_menu()  

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
            
            else:
                print("\nIncorrect option. Try again.\n")

        # REMOVE OPTION
        elif choice == "4":
            sub = ui.remove_menu()

            # REMOVE SQUAD
            if sub == "1":
                squads = squad_db.get_all_squads_names()
                ui.show_squads_names(squads)

                print("\nWrite squad name, which you want to delete\n")
                input_squad_name = ui.get_squad_name()

                if not squad_db.squad_exists(input_squad_name):
                    print("\nIncorrect squad name.\n")
                    continue

                squad_id = squad_db.get_squad_id_by_name(input_squad_name)
                squad_db.remove_squad(squad_id)
                print("\nSquad was successfully deleted.\n")
            
            # REMOVE MEMBER
            elif sub == "2":
                print("\nWrite squad name, where you want to delete member. \n")
                input_squad_name = ui.get_squad_name()

                if not squad_db.squad_exists(input_squad_name):
                    print("\nSquad doesn't exist.\n")
                    continue

                squad_id = squad_db.get_squad_id_by_name(input_squad_name)
                members = member_db.get_all_members_by_squad(squad_id)

                if not members:
                    print("\nThis squad is empty.\n")
                    continue

                for member in members:
                    ui.show_all_members(member)

                print("\nWrite member name to delete.\n")
                input_member_name = ui.get_member_name()

                if not member_db.member_exists_in_squad(input_member_name, squad_id):
                    print("\nMember doesn't exist.\n")
                    continue

                member_id = member_db.get_member_id_by_member_name_in_squad(input_member_name, squad_id)

                member_db.remove_member(member_id)
                print("\nMember was successfully deleted.\n")

            # REMOVE POWER
            elif sub == "3": 
                print("\nChooce member where you want to delete power.\n") 
                input_member_name = ui.get_member_name()

                if not member_db.member_exists(input_member_name):
                    print("\nIncorrect member name.\n")
                    continue

                member_id = member_db.get_member_id_by_name(input_member_name)
                member_powers = power_db.get_all_powers_by_member(member_id)

                if not member_powers:
                    print("\nMember doesn't have powers.\n")
                    continue

                for power in member_powers:
                    ui.show_all_powers(power)
                    
                print("\nChooce power which you want to delete\n")
                input_power_name = ui.get_power_name()

                if power_db.power_exists_in_member(input_power_name, member_id):
                    power_id = power_db.get_power_id_by_name_in_member(input_power_name, member_id)
                    power_db.remove_power(power_id)
                    print(f'\nPower: "{input_power_name}" was successfully detele.\n')
                    continue

                print("\nIncorrect power name.\n")
                    

            elif sub == "4" or sub.lower() == "b":
                continue

            elif sub == "5" or sub.lower() == "x":
                break

        # STOP
        elif choice == "5" or choice.lower() == "x":
            break

        else:
            print("\nIncorrect option. Try again.\n")

    db.close()


if __name__ == "__main__":
    main()