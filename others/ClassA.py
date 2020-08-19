class ClassA:

    def __new__(cls):
        print("ClassA.__new__")
        return super().__new__(cls)

    def __init__(self):
        print("ClassA.__init__")

    def __call__(self, *args):
        print("ClassA.__call__args", args)


if __name__ == "__main__":
    a = ClassA()
    a("arg1", "arg2")

'''
ClassA.__new__
ClassA.__init__
ClassA.__call__args ('arg1', 'arg2')
'''
