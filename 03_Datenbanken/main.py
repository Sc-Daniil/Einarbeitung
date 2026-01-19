from domain import Member, Squad
import json
import sqlite3

PATH_TO_FILE: str  = "../base.json"

base = sqlite3.connect("base.db")
cur = base.cursor()

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
    cur.execute("SELECT * FROM member")
    rows = cur.fetchone()
    ...

def main():

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

    data = get_date(PATH_TO_FILE)
    if not data:
        return

    squads = parse_squads(data)

    for squad in squads:
        safe_squads(squad)
    
    print("""

---- WELLCOME ----

          """)
    while True:
        print("""
        --- CHOICE OPTION ---
        SHOW INFO      ---> 1
        ADD DATE       ---> 2
        OVERWRITE DATE ---> 3
        REMOVE DATA    ---> 4
        LEAVE PROGRAMM ---> 5 or x
            """)
    
        choice: str = input("choice> ")

        if choice == '1':

            print("""
        -- CHOICE OPTION --
        SHOW ALL INFO ---> 1
        SHOW SQUAD    ---> 2
        SHOW MEMBERS  ---> 3
        BACK          ---> 4 or b 
        EXIT          ---> 5 or x
                   """)
            choice_info: str = input("info> ")

            while True:  
                if choice_info == '1':
                    show_all_info()
                    break
                elif choice_info == '2':
                    show_squads_info()
                    break
                elif choice_info == '3':
                    print("---Print Squad Name---")
                    squad_choice: str = input("squad> ")
                    break
                    ...

                elif choice_info == '4' or choice_info.lower() == 'b':
                    break

                elif choice_info == '5' or choice_info.lower() == 'x':
                    base.close()
                    exit()

                else:
                    print("\nIncorrect Option. Try again.\n")
                    continue

        elif choice == '2':
            ...

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


if __name__ == "__main__":
    main()
