# 监听模式-框架模型

from abc import ABCMeta, abstractmethod
# 引入ABCMeta 和 abstractmethod 来定义抽象类和抽象方法


class Observer(metaclass=ABCMeta):
    """"观察者的基类"""

    @abstractmethod
    def update(self, observable, object):
        pass


class Observable:
    """"被观察者的基类"""

    def __init__(self):
        self.__observers = []

    def addObserver(self, observer):
        self.__observers.append(observer)

    def removeObserver(self, observer):
        self.__observers.remove(observer)

    def notifyObserver(self, object=0):
        for o in self.__observers:
            o.update(self, object)
