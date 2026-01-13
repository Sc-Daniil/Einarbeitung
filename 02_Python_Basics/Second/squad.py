from member import Member

class Squad():
    """"""
    squad_name: str
    home_town: str
    formed_year: int
    secret_base: str 
    is_active: bool 
    members: list[Member]
    
    def __init__(self, squad_name, home_town, formed_year, secret_base, is_active, members) -> None:
        self.squad_name = squad_name
        self.home_town = home_town
        self.formed_year = formed_year
        self.secret_base = secret_base
        self.is_active = is_active
        self.members = members
