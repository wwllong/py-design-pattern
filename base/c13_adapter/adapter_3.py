# 适配模式-实战电子书阅读器

from abc import ABCMeta, abstractmethod, ABC
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法
import os
# 导入os库,用于文件、路径相关的解析


class Page:
    """电子书一页的内容"""

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
        self.__chapters.append(title)

    def showInfo(self):
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

    def getPageCount(self):
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

    def getPageCount(self):
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
        return self.__thirdPdf.pageSize()

    def getPage(self, pageNum):
        page = self.__thirdPdf.page(pageNum)
        print("将PdfPage的面向对象转换成Page的对象")
        return Page(page.getPageNum())


class Reader:
    """阅读器"""

    def __init__(self, name):
        self.__name = name
        self.__filePath = ""
        self.__curBook = None
        self.__curPageNum = -1

    def __initBook(self, filePath):
        self.__filePath = filePath
        extName = os.path.splitext(filePath)[1]
        if(extName.lower() == ".epub"):
            self.__curBook = EpubBook()
        elif(extName.lower() == ".txt"):
            self.__curBook = TxtBook()
        elif (extName.lower() == ".pdf"):
            self.__curBook = PdfAdapterBook(ThirdPdf())
        else:
            self.__curBook = None

    def openFile(self, filePath):
        self.__initBook(filePath)
        if(self.__curBook is not None):
            rtn = self.__curBook.parseFile(filePath)
            if(rtn):
                self.__curPageNum = 1
            return rtn
        return False

    def closeFile(self):
        print("关闭 " + self.__filePath + "文件")
        return True

    def showCatalogue(self):
        catalogue = self.__curBook.getCatalogue()
        catalogue.showInfo()

    def prePage(self):
        print("往前翻一页：", end="")
        return self.gotoPage(self.__curPageNum - 1)

    def nextPage(self):
        print("往后翻一页：", end="")
        return self.gotoPage(self.__curPageNum + 1)

    def gotoPage(self, pageNum):
        if(pageNum > 1 and pageNum < self.__curBook.getPageCount() - 1):
            self.__curPageNum = pageNum
        print("显示第" + str(self.__curPageNum) + "页")
        page = self.__curBook.getPage(self.__curPageNum)
        page.getContent()
        return page


def testReaderBase(fileName, reader):
    if (not reader.openFile(fileName)):
        return
    reader.showCatalogue()
    reader.prePage()
    reader.nextPage()
    reader.nextPage()
    reader.closeFile()
    print()


def testReader():
    reader = Reader("阅读器")
    testReaderBase("背影.txt", reader)
    testReaderBase("解忧杂货铺.epub", reader)
    testReaderBase("如何从生活中领悟设计模式.pdf", reader)


if __name__ == '__main__':
    testReader()

"""
背影.txt 文件解析成功
书名：背影
目录：
    第一章 标题
    第二章 标题
往前翻一页：显示第1页
往后翻一页：显示第2页
往后翻一页：显示第3页
关闭 背影.txt文件

解忧杂货铺.epub 文件解析成功
书名：解忧杂货铺
目录：
    第一章 标题
    第二章 标题
往前翻一页：显示第1页
往后翻一页：显示第2页
往后翻一页：显示第3页
关闭 解忧杂货铺.epub文件

第三方库解析PDF文件：如何从生活中领悟设计模式.pdf
如何从生活中领悟设计模式.pdf文件解析成功
将Outline结构的目录转换成Catalogue结构的目录
书名：如何从生活中领悟设计模式
目录：
    第一章 PDF电子书标题
    第二章 PDF电子书标题
往前翻一页：显示第1页
将PdfPage的面向对象转换成Page的对象
往后翻一页：显示第1页
将PdfPage的面向对象转换成Page的对象
往后翻一页：显示第1页
将PdfPage的面向对象转换成Page的对象
关闭 如何从生活中领悟设计模式.pdf文件

"""