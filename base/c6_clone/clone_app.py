# 实战应用 - app配置信息

from clone_frame import Clone


class AppConfig(Clone):
    """应用程序功能配置"""

    def __init__(self, configName):
        self.__configName = configName
        self.parseFromFile("./config/default.xml")

    def parseFromFile(self, filePath):
        """
        从配置文件中解析配置项
        真实项目中通过会将配置保存到配置文件中，保证下次开启时依然能够生效；
        这里为简单起见，不从文件中读取，以初始化的方式来模拟。
        """
        self.__fontType = "宋体"
        self.__fontSize = 14
        self.__language = "中文"
        self.__logPath = "./logs/appException.log"

    def saveToFile(self, filePath):
        """
        将配置保存到配置文件中
        这里为简单起见，不再实现
        """
        pass

    def copyConfig(self, configName):
        """创建一个配置的副本"""
        config = self.deepClone()
        config.__configName = configName
        return config

    def showInfo(self):
        print("%s 的配置信息如下：" % self.__configName)
        print("字体：", self.__fontType)
        print("字号：", self.__fontSize)
        print("语言：", self.__language)
        print("异常文件的路径：", self.__logPath)

    def setFontType(self, fontType):
        self.__fontType = fontType

    def setFontSize(self, fontSize):
        self.__fontSize = fontSize

    def setLanguage(self, language):
        self.__language = language

    def setLogPath(self, logPath):
        self.__logPath = logPath


def testAppConfig():
    defaultConfig = AppConfig("default")
    defaultConfig.showInfo()
    print()

    newConfig = defaultConfig.copyConfig("tonyConfig")
    newConfig.setFontType("雅黑")
    newConfig.setFontSize(18)
    newConfig.setLanguage("English")
    newConfig.showInfo()


if __name__ == "__main__":
    testAppConfig()


'''
default 的配置信息如下：
字体： 宋体
字号： 14
语言： 中文
异常文件的路径： ./logs/appException.log

tonyConfig 的配置信息如下：
字体： 雅黑
字号： 18
语言： English
异常文件的路径： ./logs/appException.log
'''