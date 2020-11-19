# 迭代模式 - 迭代器框架
class BaseIterator:
    """迭代器"""

    def __init__(self, data):
        self.__data = data
        self.toBegin()

    def toBegin(self):
        """将指针移至起始位置"""
        self.__curIdx = -1

    def toEnd(self):
        """将指针移至结尾位置"""
        self.__curIdx = len(self.__data)

    def next(self):
        """移动至下一个元素"""
        if(self.__curIdx < len(self.__data) - 1):
            self.__curIdx += 1
            return True
        else:
            return False

    def previous(self):
        """移动至上一个元素"""
        if(self.__curIdx > 0):
            self.__curIdx -= 1
            return True
        else:
            return False

    def current(self):
        """获取当前的元素"""
        return self.__data[self.__curIdx] if (self.__curIdx < len(self.__data) and self.__curIdx >= 0 ) else None


def testBaseIterator():
    print("从前往后遍历：")
    iterator = BaseIterator(range(0, 10))
    while(iterator.next()):
        customer = iterator.current()
        print(customer, end='\t')
    print()
    print("从后往前遍历")
    iterator.toEnd()
    while(iterator.previous()):
        customer = iterator.current()
        print(customer, end='\t')


if __name__ == "__main__":
    testBaseIterator()

"""
从前往后遍历：
0	1	2	3	4	5	6	7	8	9	
从后往前遍历
9	8	7	6	5	4	3	2	1	0	
"""