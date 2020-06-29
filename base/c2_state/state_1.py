# 状态模式-水的三种状态（固液气）转变-Version 1.0.0

from abc import ABCMeta, abstractmethod


class Water:
    """水"""

    def __init__(self, state):
        self.__temperature = 25  # 默认常温25°
        self.__state = state  # 状态

    def setState(self, state):
        self.__state = state

    def changeState(self, state):
        if self.__state:
            print("由", self.__state.getName(), "变为", self.__state.getName())
        else:
            print("初始化为", state.getName())
        self.__state = state

    def getTemperature(self):
        return self.__temperature

    def setTemperature(self, temperature):
        """不符合程序的开放封闭原则"""
        self.__temperature = temperature
        if self.__temperature <= 0:
            self.setState(SolidState("固态"))
        elif self.__temperature <= 100:
            self.setState(LiquidState("液态"))
        else:
            self.setState(GaseousState("气态"))

    def riseTemperature(self, step):
        self.setTemperature(self.__temperature + step)

    def reduceTemperature(self, step):
        self.setTemperature(self.__temperature - step)

    def behavior(self):
        self.__state.behavior(self)


class State(metaclass=ABCMeta):
    """状态类"""

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    @abstractmethod
    def behavior(self, water):
        """不同状态下的行为"""
        pass


class SolidState(State):
    """固态"""

    def __init__(self, name):
        super().__init__(name)

    def behavior(self, water):
        print("我性格高冷，当前体温" + str(water.getTemperature()) +
              "℃,我坚如钢铁，仿如一冷血动物，请用我砸人，嘿嘿……")


class LiquidState(State):
    """液态"""

    def __init__(self, name):
        super().__init__(name)

    def behavior(self, water):
        print("我性格温和，当前体温" + str(water.getTemperature()) +
              "℃，我可滋润万物，饮用我可让你活力倍增……")


class GaseousState(State):
    """气态"""

    def __init__(self, name):
        super().__init__(name)

    def behavior(self, water):
        print("我性格热烈，当前体温" + str(water.getTemperature()) +
              "℃，飞向天空是我毕生的梦想，在这你将看不到我的存在，我将达到无我的境界……")


def test():
    water = Water(LiquidState("液态"))
    water.behavior()
    water.setTemperature(-4)
    water.behavior()
    water.riseTemperature(18)
    water.behavior()
    water.reduceTemperature(110)
    water.behavior()


if __name__ == "__main__":
    test()

"""
我性格温和，当前体温25℃，我可滋润万物，饮用我可让你活力倍增……
我性格高冷，当前体温-4℃,我坚如钢铁，仿如一冷血动物，请用我砸人，嘿嘿……
我性格温和，当前体温14℃，我可滋润万物，饮用我可让你活力倍增……
我性格高冷，当前体温-96℃,我坚如钢铁，仿如一冷血动物，请用我砸人，嘿嘿……
"""
