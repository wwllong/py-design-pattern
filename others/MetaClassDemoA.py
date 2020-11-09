class MyClass:
    pass


if __name__ == "__main__":
    m = MyClass()
    print(type(MyClass))
    print(type(m))
    print()

    print(isinstance(m, MyClass))
    print(isinstance(MyClass, type))


"""
<class 'type'>
<class '__main__.MyClass'>

True
True
"""