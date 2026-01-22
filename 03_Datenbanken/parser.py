import json
from models import Squad, Member, Power

class Parser:
    @staticmethod
    def parse_squads(data: list) -> list:
        squads = []

        for s in data:                     
            members = []

            for m in s["members"]:         
                member = Member(
                    member_name=m["name"],
                    age=m["age"],
                    secret_identity=m["secretIdentity"],
                    powers=m["powers"],
                    squad_name=s["squadName"]
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

    @staticmethod
    def parse_members(data: list) -> list:
        list_members = []
        for s in data:
            for m in s["members"]:
                member = Member(
                    member_name=m["name"],
                    age=m["age"],
                    secret_identity=m["secretIdentity"],
                    powers=m["powers"],
                    squad_name=s["squadName"]
                )
                list_members.append(member)
        return list_members 
    
    @staticmethod
    def parse_powers(data: list) -> list:
        list_powers = []
        for s in data:
            for m in s["members"]:
                for p in m["powers"]:
                    power = Power(
                        power_name=p,
                        member_name=m["name"]
                    )
                    list_powers.append(power)
        return list_powers

    @staticmethod
    def get_data_from_file(path: str) -> dict: 
        try:
            with open(path, "r") as f:
                data = json.load(f)
            return data

        except FileNotFoundError:
            print("File not found.")
            return []

        except:
            print("Problem with JSON") 
            return []