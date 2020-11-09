# 显示指定metaclass
class CustomMetaclass(type):
    pass


class CustomClass(metaclass=CustomMetaclass):
    pass


if __name__ == "__main__":
    print(type(object))
    print(type(type))
    print()

    obj = CustomClass()
    print(type(CustomClass))
    print(type(obj))
    print(type(CustomMetaclass))

    print()
    print(isinstance(obj, CustomClass))
    print(isinstance(obj, object))

'''
<class 'type'>
<class 'type'>

<class '__main__.CustomMetaclass'>
<class '__main__.CustomClass'>
<class 'type'>

True
True
'''

