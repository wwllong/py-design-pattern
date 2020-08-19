class ClassE:
    pass


class ClassE2:

    def __call__(self, *args):
        print("This is __call__ function,args",args)


if __name__ == "__main__":
    e = ClassE()
    print(callable(e))
    e2 = ClassE2()
    print(callable(e2))
    e2("arg1","arg2")


"""
False
True
This is __call__ function,args ('arg1', 'arg2')
"""
