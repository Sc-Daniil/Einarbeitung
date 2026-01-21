from database import Database
from squad_db import SquadDB
from member_db import MemberDB
from power_db import PowerDB
from ui import UI


def main():
    db = Database("base.db")
    squad_db = SquadDB(db)
    member_db = MemberDB(db)
    power_db = PowerDB(db)
    ui = UI()

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
                squad = ui.create_squad()
                squad_db.add_squad(squad)

            elif sub == "2":
                pass 

            elif sub == "3":
                pass  

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
