# 模板模式 - 代码框架
from abc import ABCMeta, abstractmethod


class Template(metaclass=ABCMeta):
    """模板类(抽象类)"""

    @abstractmethod
    def stepOne(self):
        pass

    @abstractmethod
    def stepTwo(self):
        pass

    @abstractmethod
    def stepThree(self):
        pass

    def templateMethold(self):
        """模板方法"""
        self.stepOne()
        self.stepTwo()
        self.stepThree()


class TemplateImplA(Template):
    """模板实现类A"""

    def stepOne(self):
        print("步骤一")

    def stepTwo(self):
        print("步骤二")

    def stepThree(self):
        print("步骤三")


class TemplateImplB(Template):
    """模板实现类B"""

    def stepOne(self):
        print("Step one")

    def stepTwo(self):
        print("Step two")

    def stepThree(self):
        print("Step three")


def testTemplate():
    templateA = TemplateImplA()
    templateA.templateMethold()
    templateB = TemplateImplB()
    templateB.templateMethold()


if __name__ == '__main__':
    testTemplate()

"""
步骤一
步骤二
步骤三
Step one
Step two
Step three
"""