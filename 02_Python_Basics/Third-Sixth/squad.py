from member import Member

class Squad():
    """"""
    squad_name: str
    home_town: str
    formed_year: int
    status: str
    secret_base: str 
    is_active: bool 
    members: list[Member]
    
    def __init__(self, squad_name, home_town, formed_year, status, secret_base, is_active, members) -> None:
        self.squad_name = squad_name
        self.home_town = home_town
        self.formed_year = formed_year
        self.status = status
        self.secret_base = secret_base
        self.is_active = is_active
        self.members = members if members else []


    def squad_to_dict(self) -> dict:
        return {
            "squadName" : self.squad_name,
            "homeTown" : self.home_town,
            "formed" : self.formed_year,
            "status" : self.status,
            "secretBase" : self.secret_base,
            "active" : self.is_active,
            "members": [m.member_to_dict() for m in self.members] 
        }

    def member_to_squad(self, new_members):
        self.members.extend(new_members)

    @classmethod
    def squad_from_dict(cls, data: dict):
        members_list = [Member.member_from_dict(d) for d in data["members"]]

        return cls(
            squad_name = data["squadName"],
            home_town = data["homeTown"],
            formed_year = data["formed"],
            status = data["status"],
            secret_base = data["secretBase"],
            is_active = data["active"],
            members = members_list 
            )
    
    def __repr__(self):
        return f"""
        Name: {self.squad_name}
        Home Town: {self.home_town}
        Formed Year: {self.formed_year}
        Status: {self.status}
        Active: {self.is_active}        
        Members: {self.members} 
        """