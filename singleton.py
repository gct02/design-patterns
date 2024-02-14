class Singleton(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args, **kwargs)
        return cls.__instance

class DatabaseConnection(Singleton):
    def __init__(self):
        pass

if __name__ == "__main__":
    conn1 = DatabaseConnection()
    conn2 = DatabaseConnection()

    print(id(conn1))
    print(id(conn2))
