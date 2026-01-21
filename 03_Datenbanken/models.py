from dataclasses import dataclass

@dataclass
class Member:
    member_name: str
    age: int
    secret_identity: str
    powers: list[str]
    
@dataclass
class Squad:
    squad_name: str
    home_town: str
    formed: int
    status: str
    secret_base: str
    active: bool
    members: list[Member]