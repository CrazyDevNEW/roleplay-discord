from sqlalchemy import select
from Model.database import sync_session_factory, sync_engin
from Model.models import UserORM, Base

import time


class TestingOrm:
    @staticmethod
    def create_tables():
        sync_engin.echo = True
        Base.metadata.drop_all(sync_engin)
        Base.metadata.create_all(sync_engin)
    
    @staticmethod
    def select_users():
        with sync_session_factory() as session:
            query = select(UserORM)
            result = session.execute(query)
            return result.all()
    
    @staticmethod
    def insert_data():
        worker_bobr = UserORM(username="bobr", lastname="Chmo")
        worker_volk = UserORM(username="volk", lastname="Olegov")
        with sync_session_factory() as session:
            session.add_all([worker_bobr, worker_volk])
            session.commit()
    
    @staticmethod
    def update_data(user_id: int, username: str):
        with sync_session_factory() as session:
            worker = session.get(UserORM, user_id)
            worker.username = username
            session.commit()

if __name__ == "__main__":
    TestingOrm.create_tables()
    TestingOrm.insert_data()
    time.sleep(3)
    TestingOrm.update_data(1, "Pidrila")
