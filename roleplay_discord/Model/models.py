from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from Model.database import Base, str_25, str_50, str_230
import datetime
from typing import Annotated

intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("UTC_TIMESTAMP()"))]
updated_at = Annotated[datetime.datetime, mapped_column(
            server_default=text("UTC_TIMESTAMP()"),
            onupdate=datetime.datetime.utcnow,
            )]


class UserORM(Base):
    __tablename__ = "users"
    id: Mapped[intpk]
    username: Mapped[str_25]
    lastname: Mapped[str_25]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    links: Mapped[list["LinkORM"]] = relationship()


class LinkORM(Base):
    __tablename__ = "links"
    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id")) 
    discord_id: Mapped[int | None]
    telegramm_id: Mapped[int | None]
    mail: Mapped[str_230]
    user: Mapped["UserORM"] = relationship()
