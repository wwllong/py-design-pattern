from others.ClassA import ClassA


class ClassB:

    def __new__(cls):
        print("ClassB.__new__")
        return ClassA()
        # return super().__new__(cls)

    def __init__(self):
        print("ClassB.__init__")


if __name__ == "__main__":
    b = ClassB()
    print(type(b))

"""
ClassB.__new__
None
"""

"""
ClassB.__new__
ClassA.__new__
ClassA.__init__
<class 'others.ClassA.ClassA'>
"""