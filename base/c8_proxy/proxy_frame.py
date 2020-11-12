# 代理模式 框架
from abc import ABCMeta, abstractmethod


class Subject(metaclass=ABCMeta):
    """主题类"""

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    @abstractmethod
    def request(self, content = ''):
        pass


class RealSubject(Subject):
    """真实主题类"""

    def request(self, content):
        print("RealSubject todo something...")


class ProxySubject(Subject):
    """代理主题类"""

    def __init__(self, name, subject):
        super().__init__(name)
        self._realSubject = subject

    def request(self, content = ''):
        self.preRequest()
        if(self._realSubject is not None):
            self._realSubject.request(content)
        self.afterRequest()

    def preRequest(self):
        print("preRequest")

    def afterRequest(self):
        print("afterRequest")


def testProxy():
    realObj = RealSubject('RealSubject')
    proxyObj = ProxySubject('ProxySubject', realObj)
    proxyObj.request()


if __name__ == "__main__":
    testProxy()

"""
preRequest
RealSubject todo something...
afterRequest
"""
