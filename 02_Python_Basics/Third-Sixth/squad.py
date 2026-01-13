from member import Member

class Squad():
    """"""
    squad_name: str
    home_town: str
    status: str
    formed_year: int
    secret_base: str 
    is_active: bool 
    members: list[Member]
    
    def __init__(self, squad_name, home_town, status, formed_year, secret_base, is_active, members) -> None:
        self.squad_name = squad_name
        self.home_town = home_town
        self.status = status
        self.formed_year = formed_year
        self.secret_base = secret_base
        self.is_active = is_active
        self.members = members


    @classmethod
    def squad_from_dict(cls, data: dict):
        members_list = [Member.member_from_dict(d) for d in data["members"]]

        return cls(
            squad_name = data["squadName"],
            home_town = data["homeTown"],
            status = data["status"],
            formed_year = data["formed"],
            secret_base = data["secretBase"],
            is_active = data["active"],
            members = members_list 
            )
    
    def __repr__(self):
        return f"""
        Name: {self.squad_name}
        Home Town: {self.home_town}
        Status: {self.status}
        Formed Year: {self.formed_year}
        Active: {self.is_active}        
        Members: {self.members} 
        """