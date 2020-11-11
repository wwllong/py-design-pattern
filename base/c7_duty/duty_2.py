# 基于框架的实现
from duty_frame import Responsible, Request


class Person:
    """请求者(请假人)"""

    def __init__(self, name):
        self.__name = name
        self.__leader = None

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setLeader(self, leader):
        self.__leader = leader

    def getLeader(self):
        return self.__leader

    def sendRequest(self, request):
        print("%s 申请请假 %d 天。请假事由：%s" % (self.__name, request.getDayOff(), request.getReason()))
        if (self.__leader is not None):
            self.__leader.handleRequest(request)


class Supervisor(Responsible):
    """主管"""

    def __init__(self, name, title):
        super().__init__(name, title)

    def _handleRequestImpl(self, request):
        if (request.getDayOff() <= 2):
            print("同意 %s 请假，签字人：%s(%s)" % (request.getName(), self.getName(), self.getTitle()))


class DepartmentManager(Responsible):
    """部门总监"""

    def __init__(self, name, title):
        super().__init__(name, title)

    def _handleRequestImpl(self, request):
        if (request.getDayOff() > 2 and request.getDayOff() <= 5):
            print("同意 %s 请假，签字人：%s(%s)" % (request.getName(), self.getName(), self.getTitle()))


class CEO(Responsible):
    """CEO"""

    def __init__(self, name, title):
        super().__init__(name, title)

    def _handleRequestImpl(self, request):
        if (request.getDayOff() > 5 and request.getDayOff() <= 22):
            print("同意 %s 请假，签字人：%s(%s)" % (request.getName(), self.getName(), self.getTitle()))


class Administrator(Responsible):
    """行政人员"""

    def __init__(self, name, title):
        super().__init__(name, title)

    def _handleRequestImpl(self, request):
        print("%s 的请假申请已审核，情况属实！已备案处理。处理人：%s(%s)\n" % (request.getName(), self.getName(), self.getTitle()))


def testChainOfResponsibility():
    directLeader = Supervisor("Eren", "客户端研发部经理")
    departmentLeader = DepartmentManager("Eric", "技术研发中心总监")
    ceo = CEO("Helen", "创新文化公司CEO")
    administrator = Administrator("Nina", "行政中心总监")
    directLeader.setNextHandler(departmentLeader)
    departmentLeader.setNextHandler(ceo)
    ceo.setNextHandler(administrator)

    sunny = Person("Sunny")
    sunny.setLeader(directLeader)
    sunny.sendRequest(Request(sunny.getName(), 1, "参加MDCC大会。"))
    tony = Person("Tony")
    tony.setLeader(directLeader)
    tony.sendRequest(Request(tony.getName(), 5, "家里有紧急事情！"))
    pony = Person("Pony")
    pony.setLeader(directLeader)
    pony.sendRequest(Request(pony.getName(), 15, "出国深造。"))


if __name__ == "__main__":
    testChainOfResponsibility()

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