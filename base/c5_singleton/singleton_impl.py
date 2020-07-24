# 单例模式-实现方式


class Singleton1(object):
    """单例实现方式一：重写__new__和__init__方法"""
    __instance = None
    __isFirstInit = False

    def __new__(cls, name):
        if not cls.__instance:
            Singleton1.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name):
        if not self.__isFirstInit:
            self.__name = name
            Singleton1.__isFirstInit = True

    def getName(self):
        return self.__name


# Test1
def testSingleton1():
    tony = Singleton1("Tony")
    karry = Singleton1("Karry")
    print(tony.getName(), karry.getName())
    print("id(tony):", id(tony), "id(karry):", id(karry))
    print("tony == karry:", tony == karry)


class Singleton2(type):
    """单例实现方式二：自定义metaclass的方法"""

    def __init__(cls, what, bases=None, dict=None):
        super().__init__(what, bases, dict)
        # 初始化全局变量cls._instance为None
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        # 控制对象的创建过程，如果cls._instance为None则创建，否则直接返回
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class CustomClass(metaclass=Singleton2):
    """用户自定义的类"""

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name


# Test2
def testSingleton2():
    tony = CustomClass("Tony")
    karry = CustomClass("Karry")
    print(tony.getName(), karry.getName())
    print("id(tony):", id(tony), "id(karry):", id(karry))
    print("tony == karry:", tony == karry)


def singletonDecorator(cls, *args, **kwargs):
    """单例实现方式三：定义一个单例装饰器"""
    instance = {}

    def wrapperSingleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return wrapperSingleton


@singletonDecorator
class Singleton3:
    """使用单例装饰器修饰一个类"""

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name


# Test3
def testSingleton3():
    tony = Singleton3("Tony")
    karry = Singleton3("Karry")
    print(tony.getName(), karry.getName())
    print("id(tony):", id(tony), "id(karry):", id(karry))
    print("tony == karry:", tony == karry)


if __name__ == "__main__":
    # testSingleton1()
    # testSingleton2()
    testSingleton3()



'''
Tony Tony
id(tony): 2314241524400 id(karry): 2314241524400
tony == karry: True
'''

