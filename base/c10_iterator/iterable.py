# py的可迭代对象-生成器的方式
from collections import Iterable, Iterator
# 引入 Iterable  和 Iterator


# 使用（）定义生成器
def gen():
    """0-9的平方数"""
    return (x * x for x in range(10))


# 使用yield定义generator函数
def fibonacci(maxNum):
    """斐波那契数列的生成器"""
    a = b = 1
    for i in range(maxNum):
        # https://www.jianshu.com/p/9dd355ab4e5d
        yield a
        a, b = b, a + b


def testIsIterator():
    print("是否为Iterable对象：")
    print(isinstance([], Iterable))  # true
    print(isinstance({}, Iterable))  # true
    print(isinstance((1, 2, 3), Iterable))  # true
    print(isinstance([1, 2, 3], Iterable))  # true
    print(isinstance("string", Iterable))  # true
    print(isinstance(gen, Iterable))  # true
    print(isinstance(fibonacci(10), Iterable))  # true
    print("是否为Iterator对象：")
    print(isinstance([], Iterator))  # False
    print(isinstance({}, Iterator))  # False
    print(isinstance((1, 2, 3), Iterator))  # False
    print(isinstance([1, 2, 3], Iterator))  # False
    print(isinstance("string", Iterator))  # False
    print(isinstance(gen, Iterator))  # true
    print(isinstance(fibonacci(10), Iterator))  # true
    print(type((1, 2, 3)))  # <class 'tuple'>
    print(type(gen))  # <class 'generator'>


def testNextItem():
    print("将Iterable对象转为Iterator对象：")
    l = [1, 2, 3]
    itrL = iter(l)
    print(next(itrL))
    print(next(itrL))
    print(next(itrL))

    print("next()函数遍历迭代器元素：")
    fib = fibonacci(4)
    print(next(fib))
    print(next(fib))
    print(next(fib))
    print(next(fib))
    print(next(fib))


if __name__ == "__main__":
    gen = gen()
    for i in gen:
        print(i, end="\t")
    print()

    fib = fibonacci(10)
    for n in fib:
        print(n, end="\t")
    print()

    # 内置容器的for循环
    arr = [x * x for x in range(10)]
    for e in arr:
        print(e, end="\t")
    print()

    print()
    print(type(gen))
    print(type(fib))
    print(type(arr))

    testIsIterator()
    testNextItem()

"""
0	1	4	9	16	25	36	49	64	81	
1	1	2	3	5	8	13	21	34	55	
0	1	4	9	16	25	36	49	64	81	

<class 'generator'>
<class 'generator'>
<class 'list'>

"""
