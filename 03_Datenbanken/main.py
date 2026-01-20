from domain import Member, Squad
import json
import sqlite3

PATH_TO_FILE: str  = "../base.json"

base = sqlite3.connect("base.db")
cur = base.cursor()

# JSON - START
def parse_squads(data: list) -> list:
    squads = []

    for s in data:                     
        members = []

        for m in s["members"]:         
            member = Member(
                member_name=m["name"],
                age=m["age"],
                secret_identity=m["secretIdentity"],
                powers=m["powers"]
            )
            members.append(member)

        squad = Squad(
            squad_name=s["squadName"],
            home_town=s["homeTown"],
            formed=s["formed"],
            status=s["status"],
            secret_base=s["secretBase"],
            active=s["active"],
            members=members
        )

        squads.append(squad)

    return squads


def parse_members(data: list) -> list:
    list_members = []
    for s in data:
        for m in s["members"]:
            member = Member(
                member_name=m["name"],
                age=m["age"],
                secret_identity=m["secretIdentity"],
                powers=m["powers"]
            )
            list_members.append(member)
    return list_members 


def get_date(path: str) -> dict: 
    try:
        with open(path, "r") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print("File not found.")
        return

    except:
        print("Problem with JSON") 
        return
# JSON - END

def safe_squads(squad: Squad):
    cur.execute("SELECT squad_id FROM squads WHERE squad_name = ?", (squad.squad_name,))
    squad_row = cur.fetchone()

    if squad_row:
        squad_id = squad_row[0]
        print(f"Squad with name '{squad.squad_name}' already exists")

    else:
        cur.execute(
            "INSERT INTO squads (squad_name, home_town, formed, status, secret_base, active) VALUES (?, ?, ?, ?, ?, ?)",
            (squad.squad_name, squad.home_town, squad.formed, squad.status, squad.secret_base, squad.active)
        )
        squad_id = cur.lastrowid

        for member in squad.members:
            cur.execute(
                "INSERT INTO members (name, age, squad_id, secret_identity) VALUES (?, ?, ?, ?)",
                (member.member_name, member.age, squad_id, member.secret_identity))
            member_id = cur.lastrowid
        
            for power in member.powers:
                cur.execute(
                    "INSERT INTO powers (power, member_id) VALUES (?, ?)",
                    (power, member_id))

    base.commit()


# SHOW INFO BLOCK 
# TODO: Check if Name Squad Exist
def show_all_info() -> None:
    cur.execute("SELECT * FROM squads")
    rows = cur.fetchall()
    for squad in rows: 
        print(f"""
    >-- SQUAD --<
        Squad:       {squad[1]}
        Home Town:   {squad[2]}
        Formed:      {squad[3]}
        Status:      {squad[4]}
        Secret Base: {squad[5]}
        Active:      {bool(squad[6])}
        Members:     
        """)
        cur.execute("SELECT * FROM members WHERE squad_id = ?", (squad[0],))
        members = cur.fetchall()
        for member in members:
            print(f"""
            Name:       {member[1]}
            Age:        {member[2]}
            Secret ID:  {member[4]}
            Powers: """)
            cur.execute("SELECT * FROM powers WHERE member_id = ?", (member[0],))
            powers = cur.fetchall()
            for power in powers: 
                print(f"                - {power[1]}")
        print("\n---\n") 

def show_squads_info() -> None:
    cur.execute("SELECT * FROM squads")
    rows = cur.fetchall()
    for squad in rows: 
        print(f"""
    >-- SQUAD --<
        Squad:       {squad[1]}
        Home Town:   {squad[2]}
        Formed:      {squad[3]}
        Status:      {squad[4]}
        Secret Base: {squad[5]}
        Active:      {bool(squad[6])}
        """)

def show_member_in_squad_info(squad_name: str) -> None:
    cur.execute("SELECT squad_id FROM squads WHERE squad_name = ?", (squad_name,))
    search_id = cur.fetchone()
    cur.execute("SELECT * FROM members WHERE squad_id = ?", (search_id[0],))
    rows = cur.fetchall()
    for member in rows:
        print(f"""
    >-- MEMBER --< 
        Name:        {member[1]}
        Age:         {member[2]}
        Secret Id:   {member[3]}
        Powers: 
        """)
        cur.execute("SELECT power FROM powers WHERE member_id = ?", (member[0],))
        powers = cur.fetchall()
        for power in powers:
            print(f"             - {power[0]}")

# ADD INFO
def add_squad_sql() -> None:
    print("--- NEW SQUAD ---")
    print("Write Squad Name.")

    squad_name: str = input("name> ").strip()
    cur.execute("SELECT squad_name FROM squads WHERE squad_name = ?", (squad_name,))
    row = cur.fetchone()

    if row:
        print(f"Already exist {squad_name}")

    else:
        print("Write Squad Home Town.")
        home_town : str = input("> ")
        print("Write Squad Formed Year.")
        formed: int = input_int()
        print("Write Squad Status.")
        status: str  = input("> ")
        print("Write Squad Secret Base.") 
        secret_base: str = input("> ")
        print("Write Squad Active Status 'True/False'")
        active: bool = input_bool() 
        
        cur.execute(
            "INSERT INTO squads (squad_name, home_town, formed, status, secret_base, active) VALUES (?, ?, ?, ?, ?, ?)",
            (squad_name, home_town, formed, status, secret_base, active)
        )
        base.commit()
        
def add_member_to_squad_sql(squad_name: str) -> None:
    cur.execute("SELECT squad_id FROM squads WHERE squad_name = ?", (squad_name,))
    squad = cur.fetchone()
    if not squad:
        print("Squad doesn't exist")
        return

    squad_id = squad[0]
    print("--- NEW MEMBER ---")
    print("Write Member Name")
    name: str = input("> ")
    print("Write Member Age")
    age: int = input_int()
    print("Write Member Secret Id")
    secret_id: str = input("> ")

    cur.execute("INSERT INTO members (name, age, squad_id, secret_identity) VALUES (?, ?, ?, ?)", (name, age, squad_id, secret_id,))
    base.commit()

def add_power_to_member_sql(member_name: str) -> None:
    cur.execute("SELECT member_id FROM members WHERE name = ?", (member_name,))
    members = cur.fetchone()
    if not members:
        print("No Member Exist")
        return
    
    cur.execute(
        "INSERT INTO powers (power, member_id) VALUES (?, ?)", (members)
    )

    base.commit()

def input_int() -> int:
    while True: 
        try:
            return int(input("> "))
        except ValueError:
            print("Wrong. Write a number.")

def input_bool() -> bool:
    while True: 
        b = input("> ").strip().lower()

        if b in ["yes", "true", "y", "ja", "j", "1"]:
            return True

        elif b in ["no", "false", "n", "nein", "0"]:
            return False

        else:
            print("Incorrect value.")
            print("Use for True:  Yes/True/Ja/1")
            print("Use for False: No/False/Nein/0")
# Delete 
# ...



def make_tables():
    base.execute("""
        CREATE TABLE IF NOT EXISTS powers (
                power_id INTEGER PRIMARY KEY AUTOINCREMENT,
                power TEXT,
                member_id INTEGER,
                FOREIGN KEY(member_id) REFERENCES members(member_id)) 
    """)

    base.execute("""
        CREATE TABLE IF NOT EXISTS members (
            member_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            squad_id INTEGER,
            secret_identity TEXT,
            FOREIGN KEY(squad_id) REFERENCES squads(squad_id)   
              
        )
    """)

    base.execute("""
        CREATE TABLE IF NOT EXISTS squads (
            squad_id INTEGER PRIMARY KEY AUTOINCREMENT,
            squad_name TEXT,
            home_town TEXT,
            formed INTEGER,
            status TEXT,
            secret_base TEXT,
            active BOOLEAN
        )
    """)

# Options
def main_option() -> None:
    print("""

---- WELLCOME ----

          """)
    while True:
        print("""
        --- CHOICE OPTION ---
        SHOW INFO      ---> 1
        ADD DATA       ---> 2
        OVERWRITE DATA ---> 3
        REMOVE DATA    ---> 4
        LEAVE PROGRAMM ---> 5 or x
            """)
    
        choice: str = input("> ")

        if choice == '1':
            first_option()

        elif choice == '2':
            second_option()

        elif choice == '3':
            ...

        elif choice == '4':
            ...

        elif choice == '5' or choice.lower() == 'x':
           break

        else:
            print("\nIncorrect option. Try again.\n") 
            continue

    base.close()

def first_option() -> None:
    print("""
        -- CHOICE OPTION --
        SHOW ALL INFO ---> 1
        SHOW SQUAD    ---> 2
        SHOW MEMBERS  ---> 3
        BACK          ---> 4 or b 
        EXIT          ---> 5 or x
                   """)

    choice_info: str = input("> ")

    while True:  
        if choice_info == '1':
            show_all_info()
            break

        elif choice_info == '2':
            show_squads_info()
            break

        elif choice_info == '3':
            print("---Print Squad Name---")
            squad_choice: str = input("> ")
            show_member_in_squad_info(squad_choice)
            break

        elif choice_info == '4' or choice_info.lower() == 'b':
            break

        elif choice_info == '5' or choice_info.lower() == 'x':
            base.close()
            exit()

        else:
            print("\nIncorrect Option. Try again.\n")
            continue

def second_option() -> None:
    print("""
        -- CHOICE OPTION --
        ADD SQUAD   ---> 1
        ADD MEMBER  ---> 2
        ADD POWER   ---> 3
        BACK        ---> 4 or b
        EXIT        ---> 5 or x 
                """)
    choice_add: str = input("> ")

    while True:
        if choice_add == '1':
            add_squad_sql()
            break
            
        elif choice_add == '2':
            print("Write Squad name")
            squad_name: str = input("> ")
            add_member_to_squad_sql(squad_name)
            break

        elif choice_add == '3':
            break

        elif choice_add == '4' or choice_add.lower() == 'b':
            break
        
        elif choice_add == '5' or choice_add.lower() == 'x':
            base.close()
            exit()

        else:
            print("\nIncorrect Option. Try again.\n")
            continue

def main():
    data = get_date(PATH_TO_FILE)
    if not data:
        return

    squads = parse_squads(data)

    for squad in squads:
        safe_squads(squad)
    
    main_option()      

if __name__ == "__main__":
    main()
