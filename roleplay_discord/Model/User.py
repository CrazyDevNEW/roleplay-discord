class IUser:
    def __init__(self) -> None:
        ...

    def get_fistname(self) -> str:
        ...

    def get_lastname(self) -> str:
        ...

    def get_id(self) -> int:
        ...

    def get_exp(self) -> int:
        ...


class DiscordUser(IUser):
    def __init__(self, user_id: int, firstname: str, lastname: str, exp: int) -> None:
        self.user_id = user_id
        self.firstname = firstname
        self.lastname = lastname
        self.exp = exp

    def get_fistname(self) -> str:
        return self.firstname

    def get_lastname(self) -> str:
        return self.lastname
    
    def get_id(self) -> int:
        return self.user_id
