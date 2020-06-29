# 监听模式-智能热水器,基于监听模式框架实现-Version 2.0.0

from monitor_frame import Observable, Observer


class WaterHeater(Observable):
    """"热水器：战胜寒冬的有利武器"""

    def __init__(self):
        super().__init__()
        self.__temperature = 25

    def setTemperature(self, temperature):
        self.__temperature = temperature
        print("当前温度是：" + str(self.__temperature) + "℃")
        self.notifyObserver()

    def getTemperature(self):
        return self.__temperature


class WashingMode(Observer):
    """该模式用于洗澡"""

    def update(self, observable, object):
        if isinstance(observable, WaterHeater) and 50 <= observable.getTemperature() < 70:
            print("水已烧好！温度正好，可以用来洗澡了。")


class DrinkingMode(Observer):
    """饮用模式"""

    def update(self, observable, object):
        if isinstance(observable, WaterHeater) and observable.getTemperature() >= 100:
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
