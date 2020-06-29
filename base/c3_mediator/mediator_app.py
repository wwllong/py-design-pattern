# 中介模式应用-通信设备（麦克风、扬声器、摄像头）交互

from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法
from enum import Enum
# Python3.4 之后支持枚举Enum的语法

class DeviceType(Enum):
    "设备类型"
    TypeSpeaker = 1
    TypeMicrophone = 2
    TypeCamera = 3

class DeviceItem:
    """设备项"""

    def __init__(self, id, name, type, isDefault = False):
        self.__id = id
        self.__name = name
        self.__type = type
        self.__isDefault = isDefault

    def __str__(self):
        return "type:" + str(self.__type) + " id:" + str(self.__id) \
               + " name:" + str(self.__name) + " isDefault:" + str(self.__isDefault)

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getType(self):
        return self.__type

    def isDefault(self):
        return self.__isDefault


class DeviceList:
    """设备列表"""

    def __init__(self):
        self.__devices = []

    def add(self, deviceItem):
        self.__devices.append(deviceItem)

    def getCount(self):
        return len(self.__devices)

    def getByIdx(self, idx):
        if idx < 0 or idx >= self.getCount():
            return None
        return self.__devices[idx]

    def getById(self, id):
        for item in self.__devices:
            if( item.getId() == id):
                return item
        return None

class DeviceMgr(metaclass=ABCMeta):

    @abstractmethod
    def enumerate(self):
        """枚举设备列表
        (在程序初始化时，有设备插拔时都要重新获取设备列表)"""
        pass

    @abstractmethod
    def active(self, deviceId):
        """选择要使用的设备"""
        pass

    @abstractmethod
    def getCurDeviceId(self):
        """获取当前正在使用的设计ID"""
        pass


class SpeakerMgr(DeviceMgr):
    """扬声器设备管理类"""

    def __init__(self):
        self.__curDeviceId = None

    def enumerate(self):
        """枚举设备列表
        (真实的项目应该通过驱动程序去读取设备信息，这里只用初始化来模拟)"""
        devices = DeviceList()
        devices.add(DeviceItem("369dd760-893b-4fe0-89b1-671eca0f0224", "Realtek High Definition Audio", DeviceType.TypeSpeaker))
        devices.add(DeviceItem("59357639-6a43-4b79-8184-f79aed9a0dfc", "NVIDIA High Definition Audio", DeviceType.TypeSpeaker, True))
        return devices

    def active(self, deviceId):
        """激活指定的设备作为当前要用的设备"""
        self.__curDeviceId = deviceId

    def getCurDeviceId(self):
        return self.__curDeviceId


class DeviceUtil:
    """设备工具类"""

    def __init__(self):
        self.__mgrs = {}
        self.__mgrs[DeviceType.TypeSpeaker] = SpeakerMgr()
        # 为节省篇幅，MicrophoneMgr和CameraMgr不再实现
        # self.__microphoneMgr = MicrophoneMgr()
        # self.__cameraMgr = CameraMgr

    def __getDeviceMgr(self, type):
        return self.__mgrs[type]

    def getDeviceList(self, type):
        return self.__getDeviceMgr(type).enumerate()

    def active(self, type, deviceId):
        self.__getDeviceMgr(type).active(deviceId)

    def getCurDeviceId(self, type):
        return self.__getDeviceMgr(type).getCurDeviceId()


# Test
def testDevices():
    deviceUtil = DeviceUtil()
    deviceList = deviceUtil.getDeviceList(DeviceType.TypeSpeaker)
    print("麦克风设备列表：")
    if deviceList.getCount() > 0:
        # 设置第一个设备为要用的设备
        deviceUtil.active(DeviceType.TypeSpeaker, deviceList.getByIdx(0).getId())
    for idx in range(0, deviceList.getCount()):
        device = deviceList.getByIdx(idx)
        print(device)
    print("当前使用的设备："
          + deviceList.getById(deviceUtil.getCurDeviceId(DeviceType.TypeSpeaker)).getName())


if __name__ == "__main__":
    testDevices()


'''
麦克风设备列表：
type:DeviceType.TypeSpeaker id:369dd760-893b-4fe0-89b1-671eca0f0224 name:Realtek High Definition Audio isDefault:False
type:DeviceType.TypeSpeaker id:59357639-6a43-4b79-8184-f79aed9a0dfc name:NVIDIA High Definition Audio isDefault:True
当前使用的设备：Realtek High Definition Audio
'''