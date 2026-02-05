from enum import Enum, auto
from ui import UI
from squad_db import SquadDB
from member_db import MemberDB
from power_db import PowerDB

class Action(Enum):
    STAY = auto()
    BACK = auto()
    EXIT = auto()

class App:
    def __init__(self, ui: UI, squad_db: SquadDB, member_db: MemberDB, power_db: PowerDB):
        self.ui = ui
        self.squad_db = squad_db
        self.member_db = member_db
        self.power_db = power_db

    def run(self):
        while True:
            choice = self.ui.main_menu()
            action = self._patch_main(choice)
            if action == Action.EXIT:
                return

    def _patch_main(self, choice: str) -> Action:
        handlers = {
            "1": self.show_option,
            "2": self.add_option,
            "3": self.update_option,
            "4": self.remove_option,
            "5": self.exit_app,
            "x": self.exit_app
        }

        choice_handler = handlers.get(choice) 
        if choice_handler is None:
            print("\nIncorrect number.\n")
            return Action.STAY

        return choice_handler()


    def _run_submemu(self, menu_function, handlers: dict) -> Action:
        while True:
            output = menu_function().strip().lower()

            if output in ["b", "back"]:
                return Action.BACK

            if output in ["e", "exit"]:
                return Action.EXIT
            
            handler = handlers.get(output)
            
            if handler is None:
                print("\nIncorrect number.\n")
                continue

            action = handler() 
            
            if action == Action.BACK:
                continue
            
            if action == Action.EXIT:
                return Action.EXIT


    def show_option(self) -> Action:
        handlers = {
            "1": self.show_all,
            "2": self.show_squads,
            "3": self.show_members,
            "4": self.show_powers
        }
        
        
        action = self._run_submemu(self.ui.show_menu, handlers)
        
        if action == Action.BACK:
            return Action.STAY
        return action

    def add_option(self) -> Action:
        handlers = {
            "1": self.add_squad,
            "2": self.add_member,
            "3": self.add_power
        } 

        action = self._run_submemu(self.ui.add_menu, handlers)

        if action == Action.BACK:
            return Action.STAY
        return action

    def update_option(self) -> Action:
        handlers = {
            "1": self.update_squad,
            "2": self.update_member,
            "3": self.update_power
        }

        action = self._run_submemu(self.ui.update_menu, handlers)

        if action == Action.BACK:
            return Action.STAY
        return action

    def remove_option(self):
        handlers = {
            "1": self.remove_squad,
            "2": self.remove_member,
            "3": self.remove_power
        }

        action = self._run_submemu(self.ui.remove_menu, handlers)

        if action == Action.BACK:
            return Action.STAY
        return action
            
    
    def show_all(self) -> Action:
        squads_info = self.squad_db.get_all_squads_info()
        for squad_info in squads_info:
            self.ui.show_all_squads(squad_info)
            squad_id = squad_info[0]
            members_info = self.member_db.get_all_members_by_squad(squad_id)

            for member_info in members_info:
                self.ui.show_all_members(member_info) 
                member_id = member_info[0]
                powers_info = self.power_db.get_all_powers_by_member(member_id)

                for power_info in powers_info:
                    self.ui.show_all_powers(power_info)

        return Action.STAY
        
    def show_squads(self) -> Action:
        squads_name = self.squad_db.get_all_squads_names()
        self.ui.show_squads_names(squads_name)

        return Action.STAY 

    def show_members(self) -> Action: 
        input_squad_name = self.ui.get_squad_name()
        
        if not self.squad_db.squad_exists(input_squad_name):
            print("Incorrect squad name.")
            return Action.STAY
            
        squad_id = self.squad_db.get_squad_id_by_name(input_squad_name)
        members_names = self.member_db.get_all_member_names_in_squad(squad_id)

        self.ui.show_members_names(members_names)
        return Action.STAY

    def show_powers(self) -> Action:
        input_member_name = self.ui.get_member_name()
        
        if not self.member_db.member_exists(input_member_name):
            print("\nIncorrect member name.\n")
            return Action.STAY

        member_id = self.member_db.get_member_id_by_name(input_member_name)
        powers_names = self.power_db.get_all_powers_by_member(member_id)

        self.ui.show_powers_names(powers_names)
        return Action.STAY



    def add_squad(self) -> Action:
        squad_name = self.ui.get_squad_name()

        if self.squad_db.squad_exists(squad_name):
            print("\nSquad already exists.\n")
            return Action.STAY

        squad = self.ui.create_squad(squad_name)

        self.squad_db.add_squad(squad)
        print(f"\nNew Squad {squad_name} was added.\n")

        return Action.STAY


    def add_member(self) -> Action:
        input_member_name = self.ui.get_member_name()

        if self.member_db.member_exists(input_member_name):
            print("\nMember already exists.\n")
            return Action.STAY

        print("\nTo which squad do you want to add a member?\n")
        input_squad_name = self.ui.get_squad_name()

        squad_name_to_squad_id = self.squad_db.get_squad_id_by_name(input_squad_name)

        new_member = self.ui.create_member(input_member_name, input_squad_name) 

        self.member_db.add_member(new_member, squad_name_to_squad_id)
        print(f"\nNew Member {input_member_name} was added to {input_squad_name}.\n")

        return Action.STAY

    def add_power(self) -> Action:
        print("\nTo which member do you want to add power?\n")
        input_member_name = self.ui.get_member_name()

        if not self.member_db.member_exists(input_member_name):
            print("\nMember doesn't exist.\n")
            return Action.STAY

        member_id = self.member_db.get_member_id_by_name(input_member_name)
        print(f"\nWrite power, which you want do add to {input_member_name}.\n")
        input_power_name = self.ui.get_power_name()

        if self.power_db.power_exists_in_member(input_power_name, member_id):
            print(f"\nPower {input_power_name} already exists in member {input_member_name}\n")
            return Action.STAY

        new_power = self.ui.create_power(input_power_name, member_id)

        self.power_db.add_power(new_power, member_id)
        print(f"\nNew Power {input_power_name} added to {input_member_name}.\n")

        return Action.STAY



    def update_squad(self) -> Action:
        handlers = {
            "1": self.update_squad_name,
            "2": self.update_squad_home_town,
            "3": self.update_squad_formed,
            "4": self.update_squad_status,
            "5": self.update_squad_secret_base,
            "6": self.update_squad_active
        } 

        action = self._run_submemu(self.ui.update_squad_options, handlers)

        if action == Action.BACK:
            return Action.STAY

        return action

    def update_member(self) -> Action:
        handlers = {
            "1": self.update_member_name,
            "2": self.update_member_age,
            "3": self.update_member_secret_id
        }
        
        action = self._run_submemu(self.ui.update_member_options, handlers)

        if action == Action.BACK:
            return Action.STAY

        return action    

    def update_power(self) -> Action:

        print("\nPower updated.\n")
        return Action.STAY
    
    def update_squad_name(self):
        ...

    def update_squad_home_town(self):
        ...
    
    def update_squad_formed(self):
        ...
    
    def update_squad_status(self):
        ...

    def update_squad_secret_base(self):
        ...

    def update_squad_active(self):
        ...
    
    def update_member_name(self):
        ...

    def update_member_age(self):
        ...

    def update_member_secret_id(self):
        ...

    def remove_squad(self) -> Action:
        squads = self.squad_db.get_all_squads_names()
        self.ui.show_squads_names(squads)

        print("\nWrite squad name, which you want to delete\n")
        input_squad_name = self.ui.get_squad_name()

        if not self.squad_db.squad_exists(input_squad_name):
            print("\nIncorrect squad name.\n")
            return Action.STAY

        squad_id = self.squad_db.get_squad_id_by_name(input_squad_name)
        self.squad_db.remove_squad(squad_id)
        print("\nSquad was successfully deleted.\n")

        return Action.STAY

    def remove_member(self) -> Action:
        print("\nWrite squad name, where you want to delete member. \n")
        input_squad_name = self.ui.get_squad_name()

        if not self.squad_db.squad_exists(input_squad_name):
            print("\nSquad doesn't exist.\n")
            return Action.STAY

        squad_id = self.squad_db.get_squad_id_by_name(input_squad_name)
        members = self.member_db.get_all_members_by_squad(squad_id)

        if not members:
            print("\nThis squad is empty.\n")
            return Action.STAY

        for member in members:
            self.ui.show_all_members(member)

        print("\nWrite member name to delete.\n")
        input_member_name = self.ui.get_member_name()

        if not self.member_db.member_exists_in_squad(input_member_name, squad_id):
            print("\nMember doesn't exist.\n")
            return Action.STAY

        member_id = self.member_db.get_member_id_by_member_name_in_squad(input_member_name, squad_id)

        self.member_db.remove_member(member_id)
        print("\nMember was successfully deleted.\n")
        
        return Action.STAY

    def remove_power(self) -> Action:
        print("\nChooce member where you want to delete power.\n") 
        input_member_name = self.ui.get_member_name()

        if not self.member_db.member_exists(input_member_name):
            print("\nIncorrect member name.\n")
            return Action.STAY

        member_id = self.member_db.get_member_id_by_name(input_member_name)
        member_powers = self.power_db.get_all_powers_by_member(member_id)

        if not member_powers:
            print("\nMember doesn't have powers.\n")
            return Action.STAY

        for power in member_powers:
            self.ui.show_all_powers(power)
            
        print("\nChooce power which you want to delete\n")
        input_power_name = self.ui.get_power_name()

        if not self.power_db.power_exists_in_member(input_power_name, member_id):
            print("\nIncorrect power name.\n")
            return Action.STAY

        power_id = self.power_db.get_power_id_by_name_in_member(input_power_name, member_id)
        self.power_db.remove_power(power_id)

        print(f'\nPower: "{input_power_name}" was successfully detele.\n')
        return Action.STAY

    def exit_app(self) -> Action:
        return Action.EXIT