# 适配模式-基于框架实现电子书阅读器

from abc import ABCMeta, abstractmethod, ABC
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法
import os


# 导入os库,用于文件、路径相关的解析


class Page:
    """电子书第一页的内容"""

    def __init__(self, pageNum):
        self.__pageNum = pageNum

    def getContent(self):
        return "第 " + str(self.__pageNum) + " 页的内容"


class Catalogue:
    """目录结构"""

    def __init__(self, title):
        self.__title = title
        self.__chapters = []

    def addChapter(self, title):
        print("书名：" + self.__title)
        print("目录：")
        for chapter in self.__chapters:
            print("    " + chapter)


class IBook(metaclass=ABCMeta):
    """电子书文档的接口类"""

    @abstractmethod
    def parseFile(self, filePath):
        """解析文档"""
        pass

    @abstractmethod
    def getCatalogue(self):
        """获取目录"""
        pass

    @abstractmethod
    def getPage(self, pageNum):
        """获取第pageNum页的内容"""
        pass


class TxtBook(IBook, ABC):
    """txt解析类"""

    def parseFile(self, filePath):
        # 模拟文档的解析
        print(filePath + " 文件解析成功")
        self.__title = os.path.splitext(filePath)[0]
        self.__pageCount = 800
        return True

    def getCatalogue(self):
        catelogue = Catalogue(self.__title)
        catelogue.addChapter("第一章 标题")
        catelogue.addChapter("第二章 标题")
        return catelogue

    def getPageCount(self, pageNum):
        return self.__pageCount

    def getPage(self, pageNum):
        return Page(pageNum)


class EpubBook(IBook, ABC):
    """Epub解析类"""

    def parseFile(self, filePath):
        # 模拟文档的解析
        print(filePath + " 文件解析成功")
        self.__title = os.path.splitext(filePath)[0]
        self.__pageCount = 800
        return True

    def getCatalogue(self):
        catelogue = Catalogue(self.__title)
        catelogue.addChapter("第一章 标题")
        catelogue.addChapter("第二章 标题")
        return catelogue

    def getPageCount(self, pageNum):
        return self.__pageCount

    def getPage(self, pageNum):
        return Page(pageNum)


class Outline:
    """第三方PDF解析库的目录类"""

    def __init__(self):
        self.__outlines = []

    def addOutline(self, title):
        self.__outlines.append(title)

    def getOutlines(self):
        return self.__outlines


class PdfPage:
    """PDF页"""

    def __init__(self, pageNum):
        self.__pageNum = pageNum

    def getPageNum(self):
        return self.__pageNum


class ThirdPdf:
    """第三方PDF解析库"""

    def __init__(self):
        self.__pageSize = 0
        self.__title = ""

    def open(self, filePath):
        print("第三方库解析PDF文件：" + filePath)
        self.__title = os.path.splitext(filePath)[0]
        self.__pageCount = 1000
        return True

    def getTitle(self):
        return self.__title

    def getOutLine(self):
        outline = Outline()
        outline.addOutline("第一章 PDF电子书标题")
        outline.addOutline("第二章 PDF电子书标题")
        return outline

    def pageSize(self):
        return self.__pageSize

    def page(self, index):
        return PdfPage(index)


class PdfAdapterBook(ThirdPdf, IBook):
    """对第三方的PDF解析库重新进行包装"""

    def __init__(self, thirdPdf):
        self.__thirdPdf = thirdPdf

    def parseFile(self, filePath):
        # 模拟文档的解析
        rtn = self.__thirdPdf.open(filePath)
        if(rtn):
            print(filePath + "文件解析成功")
        return rtn

    def getCatalogue(self):
        outline = self.__thirdPdf.getOutLine()
        print("将Outline结构的目录转换成Catalogue结构的目录")
        catalogue = Catalogue(self.__thirdPdf.getTitle())
        for title in outline.getOutlines():
            catalogue.addChapter(title)
        return catalogue

    def getPageCount(self):
        return self.__thirdPdf.get

    def getPage(self, pageNum):
        """获取第pageNum页的内容"""
        pass