if __name__ == "__main__":
    ClassVar = type("ClassVar", (object,), dict(name="type test"))
    a = ClassVar()
    print(type(a))
    print(a.name)
    print(ClassVar.__bases__)

    b = 10
    print(isinstance(b, int))
    print(isinstance(b, str))
    print(isinstance(b, (int, str)))


"""
<class '__main__.ClassVar'>
type test
(<class 'object'>,)
True
False
True
"""
