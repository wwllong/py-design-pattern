# 外观模式 应用实战-压缩、解压缩系统
# 引入path，进行路径相关的处理
from os import path
# 引入logging，进行错误日志的记录
import logging


class ZIPModel:
    """ZIP模块，负责ZIP文件的压缩与解压缩，简单模拟"""

    def compress(self, srcFilePath, dstFilePath):
        print("ZIP模块正在进行 %s 文件的压缩......" % srcFilePath)
        print("文件压缩成功，已保存至 %s " % dstFilePath)

    def decompress(self, srcFilePath, dstFilePath):
        print("ZIP模块正在进行 %s 文件的解压缩....." % srcFilePath)
        print("文件解压缩成功，已保存至 %s " % dstFilePath)


class RARModel:
    """RAR模块，负责RAR文件的压缩与解压缩，简单模拟"""

    def compress(self, srcFilePath, dstFilePath):
        print("RAR模块正在进行 %s 文件的压缩......" % srcFilePath)
        print("文件压缩成功，已保存至 %s " % dstFilePath)

    def decompress(self, srcFilePath, dstFilePath):
        print("RAR模块正在进行 %s 文件的解压缩....." % srcFilePath)
        print("文件解压缩成功，已保存至 %s " % dstFilePath)


class ZModel:
    """7Z模块，负责7Z文件的压缩与解压缩，简单模拟"""

    def compress(self, srcFilePath, dstFilePath):
        print("7Z模块正在进行 %s 文件的压缩......" % srcFilePath)
        print("文件压缩成功，已保存至 %s " % dstFilePath)

    def decompress(self, srcFilePath, dstFilePath):
        print("7Z模块正在进行 %s 文件的解压缩....." % srcFilePath)
        print("文件解压缩成功，已保存至 %s " % dstFilePath)


class CompressionFacade:
    """压缩系统的外观类"""

    def __init__(self):
        self.__zipModel = ZIPModel()
        self.__rarModel = RARModel()
        self.__zModel = ZModel()

    def compress(self, srcFilePath, dstFilePath, type):
        """根据不同的压缩类型，压缩成不同的格式"""
        # 获取新的文件名
        extName = "." + type
        fullName = dstFilePath + extName
        if(type.lower() == "zip"):
            self.__zipModel.compress(srcFilePath, fullName)
        elif(type.lower() == "rar"):
            self.__rarModel.compress(srcFilePath, fullName)
        elif(type.lower() == "7z"):
            self.__zModel.compress(srcFilePath, fullName)
        else:
            logging.error("Not support this format:" + str(type))
            return False
        return True

    def decompress(self, srcFilePath, dstFilePath):
        """从srcFilePath中获取后缀，根据不同后缀名，进行不同格式的解压缩"""
        baseName = path.basename(srcFilePath)
        extName = baseName.split(".")[1]
        if (extName.lower() == "zip"):
            self.__zipModel.decompress(srcFilePath, dstFilePath)
        elif (extName.lower() == "rar"):
            self.__rarModel.decompress(srcFilePath, dstFilePath)
        elif (extName.lower() == "7z"):
            self.__zModel.decompress(srcFilePath, dstFilePath)
        else:
            logging.error("Not support this format:" + str(extName))
            return False
        return True


def testCompression():
    facade = CompressionFacade()
    facade.compress("C:/app/facade/zip.md", "C:/app/facade/zip压缩文件", "zip")
    facade.decompress("C:/app/facade/zip压缩文件.zip", "C:/app/facade/file")
    print()
    facade = CompressionFacade()
    facade.compress("C:/app/facade/rar.md", "C:/app/facade/rar压缩文件", "rar")
    facade.decompress("C:/app/facade/rar压缩文件.rar", "C:/app/facade/file")
    print()
    facade = CompressionFacade()
    facade.compress("C:/app/facade/7z.md", "C:/app/facade/7z压缩文件", "7z")
    facade.decompress("C:/app/facade/7z压缩文件.7z", "C:/app/facade/file")


if __name__ == '__main__':
    testCompression()

'''
ZIP模块正在进行 C:/app/facade/zip.md 文件的压缩......
文件压缩成功，已保存至 C:/app/facade/zip压缩文件.zip 
ZIP模块正在进行 C:/app/facade/zip压缩文件.zip 文件的解压缩.....
文件解压缩成功，已保存至 C:/app/facade/file 

RAR模块正在进行 C:/app/facade/rar.md 文件的压缩......
文件压缩成功，已保存至 C:/app/facade/rar压缩文件.rar 
RAR模块正在进行 C:/app/facade/rar压缩文件.rar 文件的解压缩.....
文件解压缩成功，已保存至 C:/app/facade/file 

7Z模块正在进行 C:/app/facade/7z.md 文件的压缩......
文件压缩成功，已保存至 C:/app/facade/7z压缩文件.7z 
7Z模块正在进行 C:/app/facade/7z压缩文件.7z 文件的解压缩.....
文件解压缩成功，已保存至 C:/app/facade/file 
'''
