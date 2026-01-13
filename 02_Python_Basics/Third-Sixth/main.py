from squad import Squad
import json


def get_data(path: str) -> list:
    try:  
        with open(path, "r") as json_data:
            data = json.loads(json_data.read())
            return data 
    except:
        print("Problem with Json")
        exit()

def squads_list(data):
    squads = [Squad.squad_from_dict(i) for i in data]
    return squads
    
def show_full_info(data) -> None:
    print([Squad.squad_from_dict(m) for m in data])


def show_squads_list(data) -> None:
    squads = squads_list(data)
    result = "\n".join(i.squad_name for i in squads)
    print(result)

def show_members_in_squad(data, squad_surch) -> None:
    squads = squads_list(data)
    for squad in squads:
        if squad_surch in squad.squad_name:
            print(squad.members)

def main_menu():
    menu_options = {
        "1" : show_full_info,
        "2" : show_squads_list,
        "3" : show_members_in_squad,
        "4" : exit 
    }
    
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
    End programm          --> 4
----------------------------------------

              """)

        choice = input("Choice> ")
        if (choice not in menu_options):
            print("Incorrect option, try again. Write something to restart.")
            input()
            continue

        if (choice == "1"):
            show_full_info(data)

        if(choice == "2"):
            show_squads_list(data)

        if(choice == "3"):
            print("Write squad name.")
            squad_choice = input("Squad> ")
            show_members_in_squad(data, squad_choice)

        if(choice == "4"):
            exit()

PATH_TO_FILE: str = "../../base.json" 
data = get_data(PATH_TO_FILE)


# show_full_info(data)
# show_squads_list(data)
# show_members_in_squad(data, "Super hero squad")
main_menu()