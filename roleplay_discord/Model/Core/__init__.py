#import datetime
#from sqlalchemy import ForeignKey
#from sqlalchemy import create_engine
#from sqlalchemy.orm import DeclarativeBase
#from sqlalchemy.orm import Mapped
#from sqlalchemy.orm import mapped_column
#from sqlalchemy.orm import relationship
#from sqlalchemy.orm import Session
#from sqlalchemy.dialects.mysql import (
#        BIGINT,
#        MEDIUMINT,
#        TINYINT,
#        DATETIME,
#        JSON,
#        TEXT,
#        )
from User import User
#
#class Base(DeclarativeBase):
#    def __repr__(self) -> str:
#        return super().__repr__()
#
#class ModelUser(Base):
#    __tablename__ = "Users"
#    _id = mapped_column("id", MEDIUMINT, primary_key=True, autoincrement=True)
#    _linked_id = mapped_column("linked_id", JSON, unique=True, nullable=False)
#    _firstname = mapped_column("firstname", TEXT(50), unique=False, nullable=False)
class Session:
    pass

class RPCore:
    def __init__(self, prefix_db: str, db_session: Session) -> None:
        self.prefix_db = prefix_db
        self.db_session = db_session

    def getUser(self, user_id: int):
        return User()

    def getWorld(self, world_name=None, world_id=None):
        return None
