from typing import Annotated
from sqlalchemy import String, create_engine
from sqlalchemy.orm import DeclarativeBase, session, sessionmaker
import config

sync_engin = create_engine(url = config.db_dsn)
sync_session_factory = sessionmaker(sync_engin)

str_25 = Annotated[str, 25]
str_50 = Annotated[str, 50]
str_230 = Annotated[str, 230]


class Base(DeclarativeBase):
    type_annotation_map = {
            str_25: String(25),
            str_50: String(50),
            str_230: String(230),
    }

    repr_cols_num = 3
    repr_cols = tuple()

    def __repr__(self) -> str:
        cols = []
        for idx, col in enumerate(self.__table__.columns.keys()):
            if col in self.repr_cols or idx < self.repr_cols_num:
                cols.append(f"{col}={getattr(self, col)}")
        
        return f"<{self.__class__.__name__} {', '.join(cols)}>"
