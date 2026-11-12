from threading import Lock, Thread


class SingletonMeta(type):
    def __new__(cls, name, bases, dct):
        return super().__new__(cls, name, bases, dct)

    def __init__(self, name, bases, dct):
        self.__instance = None
        self.__lock = Lock()
        super().__init__(name, bases, dct)

    def __call__(self, *args, **kwargs):
        with self.__lock:
            if not self.__instance:
                print("Creating the instance...")
                self.__instance = super().__call__(*args, **kwargs)
        return self.__instance


class DbConnector(metaclass=SingletonMeta):
    def getid(self):
        return id(self)


def work():
    db = DbConnector()
    print(db.getid())


if __name__ == "__main__":
    threads = [Thread(target=work) for i in range(10)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
