# 组合模式 -- 组装电脑
from abc import ABCMeta, abstractmethod


class ComputerComponent(metaclass=ABCMeta):
    """组件，所有子配件的基类"""

    def __init__(self, name):
        self._name = name

    @abstractmethod
    def showInfo(self, indent=""):
        pass

    def isComposite(self):
        return False

    def startup(self, indent=""):
        print("%s%s 准备开始工作..." % (indent, self._name))

    def shutdown(self, indent=""):
        print("%s%s 即将结束工作..." % (indent, self._name))


class CPU(ComputerComponent):
    """中央处理器"""

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent=""):
        print("%s CPU:%s, 可以进行高速计算。" % (indent, self._name))


class MemoryCard(ComputerComponent):
    """内存条"""

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent=""):
        print("%s 内存:%s, 可以缓存数据，读写速度快。" % (indent, self._name))


class HardDisk(ComputerComponent):
    """硬盘"""

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent=""):
        print("%s 硬盘:%s, 可以永久存储数据，容量大。" % (indent, self._name))


class GraphicsCard(ComputerComponent):
    """显卡"""

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent=""):
        print("%s 显卡:%s, 可以高速计算和处理图形图像。" % (indent, self._name))


class Battery(ComputerComponent):
    """电源"""

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent=""):
        print("%s 电源:%s, 可以持续给主板和外接配件供电。" % (indent, self._name))


class Fan(ComputerComponent):
    """风扇"""

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent=""):
        print("%s 风扇:%s, 辅助CPU散热。" % (indent, self._name))


class Displayer(ComputerComponent):
    """显示器"""

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent=""):
        print("%s 显示器:%s, 负责内容的显示。" % (indent, self._name))


class ComputerComposite(ComputerComponent):
    """配件组合器"""

    def __init__(self, name):
        super().__init__(name)
        self._components = []

    def showInfo(self, indent=""):
        print("%s,由以下部件组成：" % self._name)
        indent += "\t"
        for element in self._components:
            element.showInfo(indent)

    def isComposite(self):
        return True

    def addComponent(self, component):
        self._components.append(component)

    def removeComponent(self, component):
        self._components.remove(component)

    def startup(self, indent=""):
        super().startup(indent)
        indent += "\t"
        for element in self._components:
            element.startup(indent)

    def shutdown(self, indent=""):
        super().startup(indent)
        indent += "\t"
        for element in self._components:
            element.shutdown(indent)


class Mainboard(ComputerComposite):
    """主板"""

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent=""):
        print(indent + "主板:", end="")
        super().showInfo(indent)


class ComputerCase(ComputerComposite):
    """机箱"""

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent=""):
        print(indent + "机箱", end="")
        super().showInfo(indent)


class Computer(ComputerComposite):
    """电脑"""

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent=""):
        print(indent + "电脑", end="")
        super().showInfo(indent)


def testComputer():
    mainBoard = Mainboard("MSI B450I GAMING PLUS AC")
    mainBoard.addComponent(CPU("AMD Ryzen 5 3600 6-Core Processor"))
    mainBoard.addComponent(MemoryCard("Corsair DDR4 16GB x2"))
    mainBoard.addComponent(HardDisk("海康威视C2000 PRO 512G SSD"))
    mainBoard.addComponent(GraphicsCard("Radeon RX 570 Series 4G"))

    computerCase = ComputerCase("K39 v2")
    computerCase.addComponent(mainBoard)
    computerCase.addComponent(Battery("ENP 7025B FLEX 小1U 500W"))
    computerCase.addComponent(Fan("利民 AXP90R"))

    computer = Computer("wenwl ITX 主机")
    computer.addComponent(computerCase)
    computer.addComponent(Displayer("GoBiggeR 15.6 1080P"))

    computer.showInfo()
    print("\n开机过程:")
    computer.startup()
    print("\n关机过程:")
    computer.shutdown()


if __name__ == '__main__':
    testComputer()

"""
电脑wenwl ITX 主机,由以下部件组成：
	机箱K39 v2,由以下部件组成：
		主板:MSI B450I GAMING PLUS AC,由以下部件组成：
			 CPU:AMD Ryzen 5 3600 6-Core Processor, 可以进行高速计算。
			 内存:Corsair DDR4 16GB x2, 可以缓存数据，读写速度快。
			 硬盘:海康威视C2000 PRO 512G SSD, 可以永久存储数据，容量大。
			 显卡:Radeon RX 570 Series 4G, 可以高速计算和处理图形图像。
		 电源:ENP 7025B FLEX 小1U 500W, 可以持续给主板和外接配件供电。
		 风扇:利民 AXP90R, 辅助CPU散热。
	 显示器:GoBiggeR 15.6 1080P, 负责内容的显示。

开机过程:
wenwl ITX 主机 准备开始工作...
	K39 v2 准备开始工作...
		MSI B450I GAMING PLUS AC 准备开始工作...
			AMD Ryzen 5 3600 6-Core Processor 准备开始工作...
			Corsair DDR4 16GB x2 准备开始工作...
			海康威视C2000 PRO 512G SSD 准备开始工作...
			Radeon RX 570 Series 4G 准备开始工作...
		ENP 7025B FLEX 小1U 500W 准备开始工作...
		利民 AXP90R 准备开始工作...
	GoBiggeR 15.6 1080P 准备开始工作...

关机过程:
wenwl ITX 主机 准备开始工作...
	K39 v2 准备开始工作...
		MSI B450I GAMING PLUS AC 准备开始工作...
			AMD Ryzen 5 3600 6-Core Processor 即将结束工作...
			Corsair DDR4 16GB x2 即将结束工作...
			海康威视C2000 PRO 512G SSD 即将结束工作...
			Radeon RX 570 Series 4G 即将结束工作...
		ENP 7025B FLEX 小1U 500W 即将结束工作...
		利民 AXP90R 即将结束工作...
	GoBiggeR 15.6 1080P 即将结束工作...
"""
