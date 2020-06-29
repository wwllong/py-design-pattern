# 监听模式-智能热水器-Version 1.0.0

from abc import ABCMeta, abstractmethod
# 引入ABCMeta 和 abstractmethod 来定义抽象类和抽象方法


class WaterHeater:
    """热水器：战胜寒冬的有利武器"""

    def __init__(self):
        self.__observers = []  # 观察者，私有成员
        self.__temperature = 25  # 温度默认25，私有成员

    def getTemperature(self):
        return self.__temperature

    def setTemperature(self, temperature):
        self.__temperature = temperature;
        print("当前温度是：" + str(self.__temperature) + "℃")
        self.notifies()

    def addObserver(self, observer):
        self.__observers.append(observer)

    def notifies(self):
        for o in self.__observers:
            o.update(self)


class Observer(metaclass=ABCMeta):
    """洗澡模式和饮用模式的父类"""

    @abstractmethod
    def update(self, waterHeater):
        pass


class WashingMode(Observer):
    """洗澡模式"""

    def update(self, waterHeater):
        if 50 <= waterHeater.getTemperature() < 70:
            print("水已烧好！温度正好，可以用来洗澡了。")


class DrinkingMode(Observer):
    """饮用模式"""

    def update(self, waterHeater):
        if waterHeater.getTemperature() >= 100:
            print("水已烧开！可以用来饮用了。")


# test
def testWaterHeater():
    heater = WaterHeater()
    washingObser = WashingMode()
    drinkingObser = DrinkingMode()
    heater.addObserver(washingObser)
    heater.addObserver(drinkingObser)
    heater.setTemperature(40)
    heater.setTemperature(60)
    heater.setTemperature(100)


if __name__ == "__main__":
    testWaterHeater()

""""
当前温度是：40℃
当前温度是：60℃
水已烧好！温度正好，可以用来洗澡了。
当前温度是：100℃
水已烧开！可以用来饮用了。
"""
