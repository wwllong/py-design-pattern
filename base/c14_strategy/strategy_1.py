# 策略模式 - 聚会，怎么来不重要，人到就行
from abc import ABCMeta, abstractmethod


class IVehicle(metaclass=ABCMeta):
    """交通工具的抽象类"""

    @abstractmethod
    def running(self):
        pass


class SharedBicycle(IVehicle):
    """共享单车"""

    def running(self):
        print("骑共享单车（轻快便捷）", end='')


class ExpressBus(IVehicle):
    """快速公交"""

    def running(self):
        print("坐快速公交（经济绿色）", end='')


class Express(IVehicle):
    """快车"""

    def running(self):
        print("打快车（快速方便）", end='')


class Subway(IVehicle):
    """地铁"""

    def running(self):
        print("坐地铁（高效安全）", end='')


class Classmate:
    """来聚餐的同学"""

    def __init__(self, name, vehicle):
        self.__name = name
        self.__vehicle = vehicle

    def attendTheDinner(self):
        print(self.__name + " ", end='')
        self.__vehicle.running()
        print(" 来聚餐！")


def testTheDinner():
    joe = Classmate("Joe", SharedBicycle())
    joe.attendTheDinner()
    helen = Classmate("Helen", Subway())
    helen.attendTheDinner()
    henry = Classmate("Henry", ExpressBus())
    henry.attendTheDinner()
    ruby = Classmate("Ruby", Express())
    ruby.attendTheDinner()


if __name__ == '__main__':
    testTheDinner()


"""
Joe 骑共享单车（轻快便捷） 来聚餐！
Helen 坐地铁（高效安全） 来聚餐！
Henry 坐快速公交（经济绿色） 来聚餐！
Ruby 打快车（快速方便） 来聚餐！
"""