from models import Squad, Member, Power


class UI:
    def input_int(self) -> int:
        while True:
            try:
                return int(input("> "))
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
        OVERWRITE DATA ---> 3
        REMOVE DATA    ---> 4
        LEAVE PROGRAMM ---> 5 or x
        """)
        return input("> ")

    def show_menu(self) -> str:
        print("""
        SHOW ALL INFO ---> 1
        SHOW SQUAD    ---> 2
        SHOW MEMBERS  ---> 3
        BACK          ---> 4 or b
        EXIT          ---> 5 or x
        """)
        return input("> ")

    def add_menu(self) -> str:
        print("""
        ADD SQUAD   ---> 1
        ADD MEMBER  ---> 2
        ADD POWER   ---> 3
        BACK        ---> 4 or b
        EXIT        ---> 5 or x
        """)
        return input("> ")
    
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
        squad_name = input("> ").strip()
        return squad_name

    def get_member_name(self) -> str:
        print("Write member name.")
        member_name = input("> ").strip()
        return member_name
    
    def get_power_name(self) -> str:
        print("Write power name.")
        power_name = input("> ").strip()
        return power_name