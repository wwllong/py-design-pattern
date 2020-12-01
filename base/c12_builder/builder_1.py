# 构建模式 - 积木玩具，一辆车还是一个庄园
from abc import ABCMeta, abstractmethod


class Toy(metaclass=ABCMeta):
    """玩具"""

    def __init__(self, name):
        self._name = name
        self.__components = []

    def getName(self):
        return self._name

    def addComponent(self, component, count = 1, unit = "个"):
        self.__components.append([component, count, unit])
        print("%s 增加了 %d %s%s" % (self._name, count, unit, component))

    @abstractmethod
    def feature(self):
        pass


class Car(Toy):
    """小车"""

    def feature(self):
        print("我是 %s, 我可以快速奔跑······" % self._name)


class Manor(Toy):
    """庄园"""

    def feature(self):
        print("我是 %s, 可供观赏，也可用来游玩······" % self._name)


class ToyBuilder:
    """玩具构建者"""

    def buildCar(self):
        car = Car("迷你小车")
        print("正在构建 %s ······" % car.getName())
        car.addComponent("轮子", 4)
        car.addComponent("车身", 1)
        car.addComponent("发送机", 1)
        car.addComponent("方向盘")
        return car

    def buildManor(self):
        manor = Manor("淘淘小庄园")
        print("正在构建 %s ······" % manor.getName())
        manor.addComponent("客厅", 1, "间")
        manor.addComponent("卧室", 2, "间")
        manor.addComponent("书房", 1, "间")
        manor.addComponent("厨房", 1, "间")
        manor.addComponent("花园", 1)
        manor.addComponent("厕所", 1, "间")
        manor.addComponent("阳台", 1)
        manor.addComponent("围墙", 1, "堵")
        return manor


def testBuilder():
    builder = ToyBuilder()
    car = builder.buildCar()
    car.feature()

    print()
    mannor =builder.buildManor()
    mannor.feature()


if __name__ == '__main__':
    testBuilder()

"""
正在构建 迷你小车 ······
迷你小车 增加了 4 个轮子
迷你小车 增加了 1 个车身
迷你小车 增加了 1 个发送机
迷你小车 增加了 1 个方向盘
我是 迷你小车, 我可以快速奔跑······

正在构建 淘淘小庄园 ······
淘淘小庄园 增加了 1 间客厅
淘淘小庄园 增加了 2 间卧室
淘淘小庄园 增加了 1 间书房
淘淘小庄园 增加了 1 间厨房
淘淘小庄园 增加了 1 个花园
淘淘小庄园 增加了 1 间厕所
淘淘小庄园 增加了 1 个阳台
淘淘小庄园 增加了 1 堵围墙
我是 淘淘小庄园, 可供观赏，也可用来游玩······
"""