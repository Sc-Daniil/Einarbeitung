from squad import Squad
from member import Member
import json

PATH_TO_FILE: str = "../../base.json" 
CURRENT_YEAR: int = 2026

def get_data(path: str) -> list:
    try:  
        with open(path, "r") as f:
            data = json.loads(f.read())
            return data 
    except:
        print("Problem with Json")
        exit()

def squads_list(data: str):
    squads = [Squad.squad_from_dict(i) for i in data]
    return squads
    
def show_full_info(data: str) -> None:
    print([Squad.squad_from_dict(m) for m in data])


def show_squads_list(data: str) -> None:
    squads = squads_list(data)
    result = "\n".join(i.squad_name for i in squads)
    print(result)

def show_members_in_squad(data: str, squad_surch: str) -> None:
    squads = squads_list(data)
    for squad in squads:
        if squad_surch in squad.squad_name:
            print(squad.members)

def add_squad(path: str) -> None:
    try:
        with open(path, "r") as f:
            data = json.load(f)
    except:
        print("Json problem")
        exit()

    print("---Squad---")

    squad = Squad(
        squad_name = input("Squad Name: "),
        home_town = input("Squad Home Town: "),
        formed_year= int(input("Squad Formed Year: ")),
        status = input("Squad Status: "),
        secret_base = input("Squad Secret Base: "),
        is_active = True if input("Squad Active (write 'y' if squad is active): ").lower() == "y" else False,
        members = add_member() 
    )
    
    data.append(squad.squad_to_dict())
    
    with open(path, "w") as f:
        json.dump(data, f, indent = 4, ensure_ascii=False)

def add_member():
   print("---Squad's Mebmers:---")
   return Member(
       name = input("Member Name: "),
       age = int(input("Member Age: ")),
       secret_identity = input("Member Secret ID: "),
       powers = input("Member Powers (use ',' to split powers)").split(",")
   ) 
    
def main_menu(data) -> None:
    menu_options: list[str] = ["1", "2", "3", "4", "5"] 
    
    print("""

--- Welcome to program! --- 

        """)

    while True:
        print("""

Choose an option. Enter the number in the terminal
----------------------------------------
    Show Everything       --> 1
    Show Squads Name      --> 2
    Show Members in Squad --> 3
    Add New Squad         --> 4
    End programm          --> 5 
----------------------------------------

              """)

        choice = input("Choice> ")
        if (choice not in menu_options):
            print("""
--------------------------------------------------------
                  
Incorrect option, try again. Write something to restart

--------------------------------------------------------
                  """)
            input()
            continue

        if (choice == "1"):
            show_full_info(data)

        if (choice == "2"):
            show_squads_list(data)

        if (choice == "3"):
            print("Write squad name.")
            squad_choice = input("Squad> ")
            show_members_in_squad(data, squad_choice)
        
        if (choice == "4"):
            add_squad(PATH_TO_FILE)
            data = get_data(PATH_TO_FILE)
             
        if (choice == "5"):
            exit()

data = get_data(PATH_TO_FILE)


# show_full_info(data)
# show_squads_list(data)
# show_members_in_squad(data, "Super hero squad")
main_menu(data)