from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, session, sessionmaker
import config

sync_engin = create_engine(
        url = config.db_dsn,
        echo = True)

sync_session_factory = sessionmaker(sync_engin)

class Base(DeclarativeBase):
    pass
