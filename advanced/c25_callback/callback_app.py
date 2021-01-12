# 回调机制应用
# 假设有这样一个需求：求一个整数数组（如[2,3,6,9,12,15,18]）中所有的偶数并且大于10的数。
def isEvenNumber(num):
    return num % 2 == 0

def isGreaterThanTen(num):
    return num > 10

def getResultNumbers(fun, elements):
    newList = []
    for item in elements:
        if (fun(item)):
            newList.append(item)
    return newList

def testCallback():
    elements = [2, 3, 6, 9, 12, 15, 18]
    list1 = getResultNumbers(isEvenNumber, elements)
    list2 = getResultNumbers(isGreaterThanTen, elements)
    print("所有的偶数：", list1)
    print("大于10的数：", list2)

def testFilter():
    elements = [2, 3, 6, 9, 12, 15, 18]
    list1 = list(filter(lambda x: x % 2 == 0, elements))
    list2 = list(filter(lambda x: x > 10, elements))
    print("所有的偶数：", list1)
    print("大于10的数：", list2)

if __name__ == '__main__':
    testCallback()
    testFilter()

"""
所有的偶数： [2, 6, 12, 18]
大于10的数： [12, 15, 18]
所有的偶数： [2, 6, 12, 18]
大于10的数： [12, 15, 18]
"""