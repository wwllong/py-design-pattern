# 自定义metaclass创建对象过程
class CustomMetaclass(type):

    def __init__(cls, what, bases=None, dict=None):
        print("CustomMetaclass.__init__ cls:", cls)
        super().__init__(what, bases, dict)

    def __call__(cls, *args, **kwargs):
        print("CustomMetaclass.__call__ args:", args, kwargs)
        self = super(CustomMetaclass, cls).__call__(*args, **kwargs)
        print("CustomMetaclass.__call__ self:", self)
        return self


class CustomClass(metaclass=CustomMetaclass):

    def __init__(self, *args, **kwargs):
        print("CustomClass.__init__ self:", self)
        super().__init__()

    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls)
        print("CustomClass.__new__, self:", self)
        return self

    def __call__(self, *args, **kwargs):
        print("CustomClass.__call__ args:", args)


if __name__ == "__main__":
    obj = CustomClass("Meta arg1", "Meta arg2", kwarg1=1, kwarg2=2)
    print(type(CustomClass))
    print(obj)
    obj("arg1", "arg2")

'''
CustomMetaclass.__init__ cls: <class '__main__.CustomClass'>
CustomMetaclass.__call__ args: ('Meta arg1', 'Meta arg2') {'kwarg1': 1, 'kwarg2': 2}
CustomClass.__new__, self: <__main__.CustomClass object at 0x0000026532C57F40>
CustomClass.__init__ self: <__main__.CustomClass object at 0x0000026532C57F40>
CustomMetaclass.__call__ self: <__main__.CustomClass object at 0x0000026532C57F40>
<class '__main__.CustomMetaclass'>
<__main__.CustomClass object at 0x0000026532C57F40>
CustomClass.__call__ args: ('arg1', 'arg2')
'''