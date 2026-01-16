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
    cur.execute(
        "INSERT INTO squads (squad_name, home_town, formed, status, secret_base, active) VALUES (?, ?, ?, ?, ?, ?)",
        (squad.squad_name, squad.home_town, squad.formed, squad.status, squad.secret_base, squad.active)
    )

    for member in squad.members:
        cur.execute(
            "INSERT INTO members (name, age, secret_identity, powers) VALUES (?, ?, ?, ?)",
            (member.member_name, member.age, member.secret_identity, json.dumps(member.powers))
        )

    base.commit()


def main():
    base.execute("""
        CREATE TABLE IF NOT EXISTS members (
            name TEXT,
            age INTEGER,
            secret_identity TEXT,
            powers TEXT
        )
    """)

    base.execute("""
        CREATE TABLE IF NOT EXISTS squads (
            squad_name TEXT,
            home_town TEXT,
            formed INTEGER,
            status TEXT,
            secret_base TEXT,
            active BOOLEAN
        )
    """)

    base.commit()

    data = get_date(PATH_TO_FILE)
    if not data:
        return

    squads = parse_squads(data)

    for squad in squads:
        safe_squads(squad)

    base.close()


if __name__ == "__main__":
    main()
