# 单例模式-你就是我的唯一-Version 2.0.0


def singletonDecorator(cls, *args, **kwargs):
    """单例实现方式三：定义一个单例装饰器"""
    instance = {}

    def wrapperSingleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return wrapperSingleton


@singletonDecorator
class MyBeautifulGirl2(object):
    """我的漂亮女神"""

    def __init__(self, name):
        self.__name = name
        if self.__name == name:
            print("遇见" + name + "，我一见钟情！")
        else:
            print("遇见" + name + "，我置若罔闻！")

    def showMyHeart(self):
        print(self.__name + "就我心中的唯一！")


def testLove():
    jenny = MyBeautifulGirl2("Jenny")
    jenny.showMyHeart()
    kimi = MyBeautifulGirl2("Kimi")
    kimi.showMyHeart()
    print("id(jenny):", id(jenny), "id(kimi):", id(kimi))


if __name__ == "__main__":
    testLove()