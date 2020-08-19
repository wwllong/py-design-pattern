class ClassD:

    def __new__(cls):
        print("ClassB.__new__")
        self = super().__new__(cls)
        print(self)
        return self

    def __init__(self):
        print("ClassC.__init__")
        print(self)


if __name__ == "__main__":
    d = ClassD()