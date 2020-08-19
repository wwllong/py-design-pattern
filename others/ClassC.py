# class ClassC:
#
#     def __init__(self):
#         print("ClassC.__init__")
#         # return 1.0


class ClassC:

    def __new__(cls, *args, **kwargs):
        print("new", args, kwargs)
        self = super().__new__(cls)
        print(self)
        return self

    def __init__(self, *args, **kwargs):
        print("init", args, kwargs)
        print(self)


if __name__ == "__main__":
    # c = ClassC()
    c = ClassC("arg1", "arg2", a=1, b=2)


"""
TypeError: __init__() should return None, not 'float'
"""

"""
new ('arg1', 'arg2') {'a': 1, 'b': 2}
<__main__.ClassC object at 0x000001885AC17880>
init ('arg1', 'arg2') {'a': 1, 'b': 2}
<__main__.ClassC object at 0x000001885AC17880>
"""