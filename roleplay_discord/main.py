from Model.database import sync_session_factory, sync_engin
from Model.models import UserORM, Base

def create_tables():
    Base.metadata.create_all(sync_engin)

def insert_data():
    worker_bobr = UserORM(username="bobr")
    with sync_session_factory() as session:
        session.add(worker_bobr)
        session.commit()

if __name__ == "__main__":
    insert_data()
