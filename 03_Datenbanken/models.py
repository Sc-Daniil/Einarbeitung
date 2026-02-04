from dataclasses import dataclass

@dataclass
class Power:
    power_name: str
    member_name: str

@dataclass
class Member:
    member_name: str
    member_age: int
    secret_identity: str
    powers: list[str]
    squad_name: str

@dataclass
class Squad:
    squad_name: str
    home_town: str
    formed: int
    status: str
    secret_base: str
    active: bool
    members: list[Member]