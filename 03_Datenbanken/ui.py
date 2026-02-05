from models import Squad, Member, Power

class UI:
    def input_int(self) -> int:
        while True:
            try:
                return int(input("> ").strip())
            except ValueError:
                print("Wrong. Write a number.")

    def input_bool(self) -> bool:
        while True:
            b = input("> ").strip().lower()
            if b in ["yes", "true", "y", "ja", "j", "1"]:
                return True
            if b in ["no", "false", "n", "nein", "0"]:
                return False
            print("Incorrect value.")

    def main_menu(self) -> str:
        print("""

---- WELLCOME ----

        SHOW INFO      ---> 1
        ADD DATA       ---> 2
        UPDATE DATA    ---> 3
        REMOVE DATA    ---> 4
        LEAVE PROGRAMM ---> 5 or x
        """)

        return input("> ").strip().lower()

    def show_menu(self) -> str:
        print("""
        SHOW ALL INFO ---> 1
        SHOW SQUAD    ---> 2
        SHOW MEMBERS  ---> 3
        SHOW POWERS   ---> 4
        BACK          ---> b
        EXIT          ---> x
        """)

        return input("> ").strip()

    def remove_menu(self) -> str:
        print("""
        REMOVE SQUAD  ---> 1
        REMOVE MEMBER ---> 2
        REMOVE POWER  ---> 3
        BACK          ---> b
        EXIT          ---> x
        """)
        return input("> ").strip()

    def update_menu(self) -> str:
        print("""
        UPDATE SQUAD    ---> 1
        UPDATE MEMBER   ---> 2
        UPDATE POWER    ---> 3
        BACK            ---> b
        EXIT            ---> x

        """)

        return input("> ").strip()

    #region ADD
    def add_menu(self) -> str:
        print("""
        ADD SQUAD   ---> 1
        ADD MEMBER  ---> 2
        ADD POWER   ---> 3
        BACK        ---> b
        EXIT        ---> x
        """)
        return input("> ").strip()
    
    def create_squad(self, squad_name: str) -> Squad:

        print("Write Squad Home Town.")
        home_town = input("> ").strip()

        print("Write Squad Formed Year.")
        formed = self.input_int()

        print("Write Squad Status.")
        status = input("> ").strip()

        print("Write Squad Secret Base.")
        secret_base = input("> ").strip()

        print("Write Squad Active Status 'True/False'")
        active = self.input_bool()

        return Squad(
            squad_name=squad_name,
            home_town=home_town,
            formed=formed,
            status=status,
            secret_base=secret_base,
            active=active,
            members=[]
        )

    def create_member(self, member_name: str, squad_name: str) -> Member:
        print("Write Member Age")
        age = self.input_int()

        print("Write Secret Identity.")
        secret_identity = input("> ").strip()

        return Member (
            member_name=member_name,
            age=age,
            secret_identity=secret_identity,
            powers=[],
            squad_name=squad_name
        )
    
    def create_power(self, power_name: str, member_name: str) -> Power:
        return Power(
            power_name=power_name,
            member_name=member_name
        )
    
    
    def get_squad_name(self) -> str:
        print("Write squad name.")
        return input("> ").strip()

    def get_member_name(self) -> str:
        print("Write member name.")
        return input("> ").strip()
    
    def get_power_name(self) -> str:
        print("Write power name.")
        return input("> ").strip()
    
    def show_squads_names(self, squads: list) -> None:
        print("--- ALL SQUAD ---")
        for squad in squads:
            print(squad[0])
        print(f"Count Squads:  {len(squads)}")
    
    def show_members_names(self, members: list) -> None:
        print(f"--- ALL MEMBERS ---")
        for member in members:
            print(member[0])
        print(f"Count Members: {len(members)}")

    def show_powers_names(self, powers: list) -> None:
        print(f"--- ALL POWERS ---")
        for power in powers: 
            print(power[0])
        print(f"Count Powers: {len(powers)}")
        
    def show_all_squads(self, squad: tuple) -> None:
        print("-- Squad --")
        print(f"""Squad Name:    {squad[1]}
Home Town:     {squad[2]}
Formed:        {squad[3]}
Status:        {squad[4]}
Secret Base:   {squad[5]}
Active:        {bool(squad[6])}
""")

    def show_all_members(self, member: tuple) -> None: 
        print(f"""    Member Name:    {member[1]}
    Age:            {member[2]}
    Secret Id:      {member[4]}
    """)

    def show_all_powers(self, power: tuple) -> None:
        print(f"       Power: {power[0]} \n")

    def update_squad_options(self) -> str:
        print("""
        UPDATE SQUAD NAME            ---> 1
        UPDATE SQUAD HOME TOWN       ---> 2
        UPDATE SQUAD FORMED YEAR     ---> 3
        UPDATE SQUAD STATUS          ---> 4
        UPDATE SQUAD SECRET BASE     ---> 5
        UPDATE SQUAD ACTIVE STATE    ---> 6
        BACK                         ---> b
        EXIT                         ---> x
        """)

        return input("> ").strip()
    
    def update_member_options(self) -> str:
        print("""
        UPDATE MEMBER NAME        ---> 1
        UPDATE MEMBER AGE         ---> 2
        UPDATE MEMBER SECRET ID   ---> 3
        BACK                      ---> b
        EXIT                      ---> x
        """)

        return input("> ").strip()
    