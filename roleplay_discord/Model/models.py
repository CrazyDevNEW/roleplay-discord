from sqlalchemy import Column
from sqlalchemy.types import String
from Model.database import Base
from sqlalchemy.orm import Mapped, mapped_column

class UserORM(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username = Column(String(20))
    lastname = Column(String(25))
