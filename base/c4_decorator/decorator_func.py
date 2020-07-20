# Python 中的装饰器 - 修饰函数


def func(num):
    """定义内部函数并返回"""

    def firstInnerFunc():
        return "这是第一个内部函数"

    def secondInnerFunc():
        return "这是第二个内部函数"

    if num == 1:
        return firstInnerFunc
    else:
        return secondInnerFunc


if __name__ == "__main__":
    print(func(1))
    print(func(2))
    print(func(1)())
    print(func(2)())
    print()
    firstFunc = func(1)
    secondFunc = func(2)
    print(firstFunc)
    print(secondFunc)
    print(firstFunc())
    print(secondFunc())

'''
<function func.<locals>.firstInnerFunc at 0x0000018EE8332598>
<function func.<locals>.secondInnerFunc at 0x0000018EE8332620>
这是第一个内部函数
这是第二个内部函数

<function func.<locals>.firstInnerFunc at 0x0000018EE8332598>
<function func.<locals>.secondInnerFunc at 0x0000018EE83326A8>
这是第一个内部函数
这是第二个内部函数
'''