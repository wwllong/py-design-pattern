# 代理模式2.0 - 基于框架框架代收快递
from proxy_frame import Subject, ProxySubject


class TonyReception(Subject):
    """Tony 接收"""

    def __init__(self, name, phoneNum):
        super().__init__(name)
        self.__phoneNum = phoneNum

    def getPhoneNum(self):
        return self.__phoneNum

    def request(self, content = ''):
        print("货物主人：%s, 手机号：%s" % (self.getName(), self.getPhoneNum()))
        print("接受到一个包裹, 包裹内容：%s" % str(content))


class WendyReception(ProxySubject):
    """Wendy 代收"""

    def __init__(self, name, receiver):
        super().__init__(name, receiver)

    def preRequest(self):
        print("我是%s的朋友，我来帮他代收快递 " % (self._realSubject.getName() + ""))

    def afterRequest(self):
        print("代收人：%s" % self.getName())


def testReceiveParcel():
    tony = TonyReception("Tony", "18812345678")
    print("Tony 接收：")
    tony.request("雪地靴")
    print()

    print("Wendy 代收：")
    wendy = WendyReception("Wendy", tony)
    wendy.request("雪地靴")


if __name__ == "__main__":
    testReceiveParcel()

"""
Tony 接收：
货物主人：Tony, 手机号：18812345678
接受到一个包裹, 包裹内容：雪地靴

Wendy 代收：
我是Tony的朋友，我来帮他代收快递 
货物主人：Tony, 手机号：18812345678
接受到一个包裹, 包裹内容：雪地靴
代收人：Wendy
"""