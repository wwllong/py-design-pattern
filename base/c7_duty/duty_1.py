# 职责模式 Version 1.0 请假流程
from abc import ABCMeta, abstractmethod


class Person:
    """请假申请人"""
    def __init__(self, name, dayoff, reason):
        self.__name = name
        self.__dayoff = dayoff
        self.__reason = reason
        self.__leader = None

    def getName(self):
        return self.__name

    def getDayOff(self):
        return self.__dayoff

    def getReason(self):
        return self.__reason

    def setLeader(self, leader):
        self.__leader = leader

    def request(self):
        print("%s 申请请假 %d 天。请假事由：%s" % (self.__name, self.__dayoff, self.__reason))
        if self.__leader is not None:
            self.__leader.handleRequest(self)


class Manager(metaclass=ABCMeta):
    """公司管理人员-基类"""

    def __init__(self, name, title):
        self.__name = name
        self.__title = title
        self._nextHandler = None

    def getName(self):
        return self.__name

    def getTitle(self):
        return self.__title

    def setNextHandler(self, nextHandler):
        self._nextHandler = nextHandler

    @abstractmethod
    def handleRequest(self, person):
        pass


class Supervisor(Manager):
    """主管"""

    def __init__(self, name, title):
        super().__init__(name, title)

    def handleRequest(self, person):
        if(person.getDayOff() <= 2):
            print("同意 %s 请假，签字人：%s(%s)" % (person.getName(), self.getName(), self.getTitle()))
        if(self._nextHandler is not None):
            self._nextHandler.handleRequest(person)


class DepartmentManager(Manager):
    """部门总监"""
    def __init__(self, name, title):
        super().__init__(name, title)

    def handleRequest(self, person):
        if(person.getDayOff() >2 and person.getDayOff() <= 5):
            print("同意 %s 请假，签字人：%s(%s)" % (person.getName(), self.getName(), self.getTitle()))
        if(self._nextHandler is not None):
            self._nextHandler.handleRequest(person)


class CEO(Manager):
    """CEO"""

    def __init__(self, name, title):
        super().__init__(name, title)

    def handleRequest(self, person):
        if (person.getDayOff() > 5 and person.getDayOff() <= 22):
            print("同意 %s 请假，签字人：%s(%s)" % (person.getName(), self.getName(), self.getTitle()))
        if (self._nextHandler is not None):
            self._nextHandler.handleRequest(person)


class Administrator(Manager):
    """行政人员"""

    def __init__(self, name, title):
        super().__init__(name, title)

    def handleRequest(self, person):
        print("%s 的请假申请已审核，情况属实！已备案处理。处理人：%s(%s)\n" % (person.getName(), self.getName(), self.getTitle()))


def testAskForLeave():
    directLeader = Supervisor("Eren", "客户端研发部经理")
    departmentLeader = DepartmentManager("Eric", "技术研发中心总监")
    ceo = CEO("Helen", "创新文化公司CEO")
    administrator = Administrator("Nina", "行政中心总监")
    directLeader.setNextHandler(departmentLeader)
    departmentLeader.setNextHandler(ceo)
    ceo.setNextHandler(administrator)

    sunny = Person("Sunny", 1, "参加MDCC大会。")
    sunny.setLeader(directLeader)
    sunny.request()
    tony = Person("Tony", 5, "家里有紧急事情！")
    tony.setLeader(directLeader)
    tony.request()
    pony = Person("Pony", 15, "出国深造。")
    pony.setLeader(directLeader)
    pony.request()


if __name__ == "__main__":
    testAskForLeave()

'''
Sunny 申请请假 1 天。请假事由：参加MDCC大会。
同意 Sunny 请假，签字人：Eren(客户端研发部经理)
Sunny 的请假申请已审核，情况属实！已备案处理。处理人：Nina(行政中心总监)

Tony 申请请假 5 天。请假事由：家里有紧急事情！
同意 Tony 请假，签字人：Eric(技术研发中心总监)
Tony 的请假申请已审核，情况属实！已备案处理。处理人：Nina(行政中心总监)

Pony 申请请假 15 天。请假事由：出国深造。
同意 Pony 请假，签字人：Helen(创新文化公司CEO)
Pony 的请假申请已审核，情况属实！已备案处理。处理人：Nina(行政中心总监)
'''