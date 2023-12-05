class IUser:
    def __init__(self) -> None:
        ...

    @property
    def fistname(self) -> str:
        ...

    @property
    def lastname(self) -> str:
        ...
        
    @property
    def id(self) -> int:
        ...


class DiscordUser(IUser):
    def __init__(self, user_id: int, firstname: str, lastname: str) -> None:
        ...

    @property
    def fistname(self) -> str:
        return self.firstname

    @property
    def lastname(self) -> str:
        return self.lastname
    
    @property
    def id(self) -> int:
        return self.user_id
