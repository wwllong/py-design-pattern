def funTest(name):
    print("This is test function, name", name)


if __name__ == "__main__":
    print(callable(filter))
    print(callable(max))
    print(callable(object))
    print(callable(funTest))
    var = "Test"
    print(callable(var))
    funTest("Python")

"""
True
True
True
True
False
This is test function, name Python
"""