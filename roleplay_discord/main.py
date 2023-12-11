import time

if __name__ == "__main__":
    TestingOrm.create_tables()
    TestingOrm.insert_data()
    time.sleep(3)
    TestingOrm.update_data(1, "Pidrila")
