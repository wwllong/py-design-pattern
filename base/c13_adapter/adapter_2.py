# 适配模式-插座适配器

from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法


class SocketEntity:
    """插座接口类型定义"""

    def __init__(self, numOfPin, typeOfPin):
        self.__numOfPin = numOfPin  # 针数
        self.__typeOfPin = typeOfPin  # 插座类型

    def getNumOfPin(self):
        return self.__numOfPin

    def setNumOfPin(self, numOfPin):
        self.__numOfPin = numOfPin

    def getTypeOfPin(self):
        return self.__typeOfPin

    def setTypeOfPin(self, typeOfPin):
        self.__typeOfPin = typeOfPin


class ISocket(metaclass=ABCMeta):
    """插座类型"""

    def getName(self):
        """插座名称"""
        pass

    def getSocket(self):
        """获取接口"""
        pass


class ChineseSocket(ISocket):
    """国标插座"""

    def getName(self):
        return "国标插座"

    def getSocket(self):
        return SocketEntity(3, "八字扁型")


class BritishSocket:
    """英标插座"""

    def name(self):
        return "英标插座"

    def socketInterface(self):
        return SocketEntity(3, "T字方型")


class AdapterSocket(ISocket):
    """插座转换器"""

    def __init__(self, britishSocket):
        self.__britishSocket = britishSocket

    def getName(self):
        return self.__britishSocket.name() + "转换器"

    def getSocket(self):
        socket = self.__britishSocket.socketInterface()
        socket.setTypeOfPin("八字扁型")
        return socket


def canChargeforDigtalDevice(name, socket):
    if socket.getNumOfPin() == 3 and socket.getTypeOfPin() == "八字扁型":
        isStandard = "符合"
        canCharge = "可以"
    else:
        isStandard = "不符合"
        canCharge = "不能"

    print("[%s]：\n针脚数量：%d，针脚类型：%s； %s中国标准，%s给大陆的电子设备充电！"
          % (name, socket.getNumOfPin(), socket.getTypeOfPin(), isStandard, canCharge))


def testSocket():
    chineseSocket = ChineseSocket()
    canChargeforDigtalDevice(chineseSocket.getName(), chineseSocket.getSocket())

    britishSocket = BritishSocket()
    canChargeforDigtalDevice(britishSocket.name(), britishSocket.socketInterface())

    adapterSocket = AdapterSocket(britishSocket)
    canChargeforDigtalDevice(adapterSocket.getName(), adapterSocket.getSocket())


if __name__ == "__main__":
    testSocket()

"""
[国标插座]：
针脚数量：3，针脚类型：八字扁型； 符合中国标准，可以给大陆的电子设备充电！
[英标插座]：
针脚数量：3，针脚类型：T字方型； 不符合中国标准，不能给大陆的电子设备充电！
[英标插座转换器]：
针脚数量：3，针脚类型：八字扁型； 符合中国标准，可以给大陆的电子设备充电！
"""