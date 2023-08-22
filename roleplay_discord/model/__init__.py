from sqlalchemy.orm import Session

class RolePlayCore:
    def __init__(self, prefix_db: str, db_session: Session) -> None:
        self.prefix_db = prefix_db
        self.db_session = db_session

    async def getUser(self, user_id: int):
        return None

    async def getWorld(self, world_name=None, world_id=None):
        return None
