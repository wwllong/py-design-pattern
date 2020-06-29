# 适配模式-身高不够鞋来凑

from abc import ABCMeta, abstractmethod


# 引入ABCMeta 和 abstractmethod 来定义抽象类和抽象方法

class IHightPerson(metaclass=ABCMeta):
    """接口类"""

    @abstractmethod
    def getName(self):
        """获取姓名"""
        pass

    @abstractmethod
    def getHeight(self):
        """获取身高"""
        pass

    @abstractmethod
    def appearance(self, person):
        """外貌"""
        pass


class HighPerson(IHightPerson):
    """个高的人"""

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def getHeight(self):
        return 170

    def appearance(self):
        print(self.getName() + "身高" + str(self.getHeight()) + "，完美如你，天生的美女！")


class ShortPerson:
    """个矮的人"""

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def getRealHeight(self):
        return 160

    def getShoesHeight(self):
        return 6


class DecoratePerson(ShortPerson, IHightPerson):
    """有高跟鞋搭配的人"""

    def __init__(self, name):
        super().__init__(name)

    def getName(self):
        return super().getName()

    def getHeight(self):
        return super().getRealHeight() + super().getShoesHeight()

    def appearance(self):
        print(self.getName() + "身高" + str(self.getHeight()) + ", 在高跟鞋的适配下，你身高不输高圆圆，气质不输范冰冰！")


class HeightMatch:
    """身高匹配"""

    def __init__(self, person):
        self.__person = person

    def matching(self, person1):
        """假设标准身高差为10厘米内"""
        distance = abs(self.__person.getHeight() - person1.getHeight())
        isMatch = distance <= 10
        print(self.__person.getName() + "和" + person1.getName() + "是否为情侣的标准身高差："
              + ("是" if isMatch else "否") + ", 差值：" + str(distance))


class Hotel:
    """(高级)酒店"""

    def recruit(self, person):
        """
        聘用
        :param person: IHightPerson的对象
        """
        suitable = self.receptionistSuitable(person)
        print(person.getName() + "是否适合做接待员：", "符合" if suitable else "不符合")

    def receptionistSuitable(self, person):
        """
        是否可以成为(高级酒店)接待员
        :param person: IHightPerson的对象
        :return: 是否符合做接待员的条件
        """
        return person.getHeight() >= 165


def testPerson():
    lira = HighPerson("Lira")
    lira.appearance()
    demi = DecoratePerson("Demi");
    demi.appearance()

    haigerMatching = HeightMatch(HighPerson("Haiger"))
    haigerMatching.matching(lira)
    haigerMatching.matching(demi)

    hotel = Hotel()
    hotel.recruit(lira)
    hotel.recruit(demi)


if __name__ == "__main__":
    testPerson()
