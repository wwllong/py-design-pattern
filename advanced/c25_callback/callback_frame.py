# 回调机制 - 框架模式，面向过程的实现方式
def callback(*args, **kwargs):
    """回调函数"""
    # todo 函数体的实现


def otherFun(fun, *args, **kwargs):
    """高阶函数，也叫包含函数"""
    # todo 函数体的实现

# 函数的调用方式
otherFun(callable)


# 回调机制 - 框架模式，面向对象的实现方式
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法


class Strategy(metaclass=ABCMeta):
    """算法的抽象类"""

    @abstractmethod
    def algorithm(self, *args, **kwargs):
        """定义算法"""
        pass


class StrategyA(Strategy):
    """策略A"""

    def algorithm(self, *args, **kwargs):
        print("算法A的实现...")


class StrategyB(Strategy):
    """策略B"""

    def algorithm(self, *args, **kwargs):
        print("算法B的实现...")


class Context:
    """上下文环境类"""

    def interface(self, strategy, *args, **kwargs):
        """交互接口"""
        print("回调执行前的操作")
        strategy.algorithm()
        print("回调执行后的操作")


# 调用方式
context = Context()
context.interface(StrategyA())
context.interface(StrategyB())