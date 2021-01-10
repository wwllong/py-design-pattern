# 对象池技术 - 共享充电宝基于框架实现
from object_pool_frame import ObjectPool, PooledObject


class PowerBank:
    """移动电源"""

    def __init__(self, serialNum, electricQuantity):
        self.__serialNum = serialNum
        self.__electricQuantity = electricQuantity
        self.__user = ""

    def getSerialNum(self):
        return self.__serialNum

    def getElectricQuantity(self):
        return self.__electricQuantity

    def setUser(self, user):
        self.__user = user

    def getUser(self):
        return self.__user

    def showInfo(self):
        print("序列号:%03d  电量:%d%%  使用者:%s" % (self.__serialNum, self.__electricQuantity, self.__user))


class PowerBankPool(ObjectPool):
    """存放移动电源的智能箱盒"""

    __serialNum = 0

    @classmethod
    def getSerialNum(cls):
        cls.__serialNum += 1
        return cls.__serialNum


    def createPooledObject(self):
        powerBank = PowerBank(PowerBankPool.getSerialNum(), 100)
        return PooledObject(powerBank)


def testObjectPool():
    powerBankPool = PowerBankPool()
    powerBank1 = powerBankPool.borrowObject()
    if (powerBank1 is not None):
        powerBank1.setUser("Tony")
        powerBank1.showInfo()
    powerBank2 = powerBankPool.borrowObject()
    if (powerBank2 is not None):
        powerBank2.setUser("Sam")
        powerBank2.showInfo()
    powerBankPool.returnObject(powerBank1)
    # powerBank1归还后，不能再对其进行相关操作
    powerBank3 = powerBankPool.borrowObject()
    if (powerBank3 is not None):
        powerBank3.setUser("Aimee")
        powerBank3.showInfo()

    powerBankPool.returnObject(powerBank2)
    powerBankPool.returnObject(powerBank3)
    powerBankPool.clear()


if __name__ == '__main__':
    testObjectPool()

"""
INFO:root:1d63d824e50对象已被借用, time:2021-01-10 17:20:28
序列号:001  电量:100%  使用者:Tony
INFO:root:1d63d824f10对象已被借用, time:2021-01-10 17:21:02
序列号:002  电量:100%  使用者:Sam
INFO:root:1d63d824e50对象已归还, time:2021-01-10 17:21:08
INFO:root:1d63d824e50对象已被借用, time:2021-01-10 17:21:21
序列号:001  电量:100%  使用者:Aimee
INFO:root:1d63d824f10对象已归还, time:2021-01-10 17:21:31
INFO:root:1d63d824e50对象已归还, time:2021-01-10 17:21:43
"""