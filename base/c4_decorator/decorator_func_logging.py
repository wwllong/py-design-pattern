# Python 中的装饰器 - 修饰函数,记录日志的装饰器

import logging
logging.basicConfig(level=logging.INFO)


def loggingDecorator(func):
    """记录日志的装饰器"""

    def wrapperLogging(*args, **kwargs):
        logging.info("开始执行 %s()... " % func.__name__)
        func(*args, **kwargs)
        logging.info("%s() 执行完成... " % func.__name__)
    return wrapperLogging


def showInfo(*args, **kwargs):
    """
    :param args: *args 表示把传进来的位置参数都装在元组 args 里面
    :param kwargs:  **kwargs 就是针对关键字参数和字典
    :return:
    """
    print("这是一个测试函数，参数: ", args, kwargs)


@loggingDecorator
def showSum(a, b):
    print("%d、%d 中的和是：%d" % (a, b, a + b))


if __name__ == "__main__":
    decoratedShowInfo = loggingDecorator(showInfo)
    decoratedShowInfo('arg1', 'arg2', kwarg1=1, kwarg2=2)
    showSum(777, 3)

'''
这是一个测试函数，参数:  ('arg1', 'arg2') {'kwarg1': 1, 'kwarg2': 2}
777、3 中的和是：780
INFO:root:开始执行 showInfo()... 
INFO:root:showInfo() 执行完成... 
INFO:root:开始执行 showSum()... 
INFO:root:showSum() 执行完成... 
'''

''' python的 * 和 **

调用函数时使用*和 **
假设有函数  def test(a, b, c)
1. test(*args)：* 的作用其实就是把序列 args 中的每个元素，当作位置参数传进去。比如上面这个代码，如果 args 等于 (1,2,3) ，那么这个代码就等价于 test(1, 2, 3) 。
2. test(**kwargs)：** 的作用则是把字典 kwargs 变成关键字参数传递。比如上面这个代码，如果 kwargs 等于 {‘a’:1,’b’:2,’c’:3} ，那这个代码就等价于 test(a=1,b=2,c=3) 。

定义函数参数时使用*和**
def test(*args):
　　定义函数参数时 * 的含义又要有所不同，在这里 *args 表示把传进来的位置参数都装在元组 args 里面。比如说上面这个函数，调用 test(1, 2, 3) 的话， args 的值就是 (1, 2, 3) 。:
def test(**kwargs):
　　类似的， ** 就是针对关键字参数和字典的了。 调用 test(a=1,b=2,c=3) 的话， kwargs 的值就是 {‘a’:1,’b’:2,’c’:3} 了。

'''