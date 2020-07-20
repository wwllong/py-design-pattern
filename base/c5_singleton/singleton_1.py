# 单例模式-你就是我的唯一-Version 1.0.0


class MyBeautifulGril(object):
    """我的漂亮女神"""
    __instance = None
    __isFirstInit = False

    def __new__(cls, name):
        if not cls.__instance:
            MyBeautifulGril.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name):
        if not self.__isFirstInit:
            self.__name = name
            print("遇见" + name + "，我一见钟情！")
            MyBeautifulGril.__isFirstInit = True
        else:
            print("遇见" + name + "，我置若罔闻！")

    def showMyHeart(self):
        print(self.__name + "就我心中的唯一！")