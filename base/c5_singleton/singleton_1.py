# 单例模式-你就是我的唯一-Version 1.0.0


class MyBeautifulGirl(object):
    """我的漂亮女神"""
    __instance = None
    __isFirstInit = False

    def __new__(cls, name):
        if not cls.__instance:
            MyBeautifulGirl.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name):
        if not self.__isFirstInit:
            self.__name = name
            print("遇见" + name + "，我一见钟情！")
            MyBeautifulGirl.__isFirstInit = True
        else:
            print("遇见" + name + "，我置若罔闻！")

    def showMyHeart(self):
        print(self.__name + "就我心中的唯一！")


def testLove():
    jenny = MyBeautifulGirl("Jenny")
    jenny.showMyHeart()
    kimi = MyBeautifulGirl("Kimi")
    kimi.showMyHeart()
    print("id(jenny):", id(jenny), "id(kimi):", id(kimi))


if __name__ == "__main__":
    testLove()


'''
遇见Jenny，我一见钟情！
Jenny就我心中的唯一！
遇见Kimi，我置若罔闻！
Jenny就我心中的唯一！
id(jenny): 1721453617784 id(kimi): 1721453617784
'''



