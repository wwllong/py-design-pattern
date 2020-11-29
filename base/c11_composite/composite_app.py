# 组合模式 - 应用，遍历文件夹下所有目录

import os
from composite_frame import Component, Composite


class FileDetail(Component):
    """文件详情"""

    def __init__(self, name):
        super().__init__(name)
        self._size = 0

    def setSize(self, size):
        self._size = size

    def getFileSize(self):
        return self._size

    def feature(self, indent):
        # 文件大小，单位：kb， 精确度：2位小数
        fileSize = round(self._size / float(1024), 2)
        print("文件名称：%s，文件大小：%sKB" % (self._name, fileSize))


class FolderDetail(Composite):
    """文件夹详情"""

    def __init__(self, name):
        super().__init__(name)
        self._count = 0

    def setCount(self, fileNum):
        self._count = fileNum

    def getCount(self):
        return self._count

    def feature(self, indent):
        print("文件夹名：%s， 文件数量：%d， 包含的文件：" % (self._name, self._count))
        super().feature(indent)


def scanDir(rootPath, folderDetail):
    """扫描某一文件夹下的所有目录"""
    if not os.path.isdir(rootPath):
        raise ValueError("rootPath不是有效的路径：%s" % rootPath)
    if folderDetail is None:
        raise ValueError("folderDetail不能为空！")

    fileNames = os.listdir(rootPath)
    for fileName in fileNames:
        filePath = os.path.join(rootPath, fileName)
        if os.path.isdir(filePath):
            folder = FolderDetail(fileName)
            scanDir(filePath, folder)
            folderDetail.addComponent(folder)
        else:
            fileDetail = FileDetail(fileName)
            fileDetail.setSize(os.path.getsize(filePath))
            folderDetail.addComponent(fileDetail)
            folderDetail.setCount(folderDetail.getCount() + 1)


if __name__ == '__main__':
    folder = FolderDetail("组合模式")
    scanDir("C:/app/WorkSpace/PyCharm/py-design-pattern/base/c11_composite", folder)
    folder.feature("")


"""
文件夹名：组合模式， 文件数量：3， 包含的文件：
	文件名称：composite_1.py，文件大小：6.41KB
	文件名称：composite_app.py，文件大小：2.32KB
	文件名称：composite_frame.py，文件大小：0.95KB
	文件夹名：__pycache__， 文件数量：1， 包含的文件：
		文件名称：composite_frame.cpython-38.pyc，文件大小：1.89KB
"""