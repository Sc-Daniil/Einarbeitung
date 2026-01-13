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

    @classmethod
    def member_from_dict(cls, data: dict):
        return cls(
            name = data["name"],
            age = data["age"],
            secret_identity = data["secretIdentity"],
            powers = data["powers"] 
        )

    def __repr__(self):
        list_powers = ", ".join(self.powers)

        return f"""
            Name: {self.name}
            Age: {self.age}
            Secret Identity: {self.secret_identity}
            Powers: {list_powers}
            """