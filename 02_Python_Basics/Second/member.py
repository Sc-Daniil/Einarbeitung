class Member():
    """"""
    name: str
    age: int
    secret_identity: str
    powers: list[str]

    def __init__(self, name, age, secret_identity, powers):
        self.name = name
        self.age = age
        self.secret_identity = secret_identity
        self.powers = powers
