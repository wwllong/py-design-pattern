# 里氏替换原则，Liskov Substitution Principle
from principle.OCP import TerrestrialAnimal, AquaticAnimal, BirdAnimal


class Monkey(TerrestrialAnimal):
    """猴子"""

    def __init__(self, name):
        super().__init__(name)

    def climbing(self):
        print(self._name + "在爬树，动作灵活轻盈...")


# 修改Zoo类，增加climbing方法：
class Zoo:
    """动物园"""

    def __init__(self):
        self.__animals =[]

    def addAnimal(self, animal):
        self.__animals.append(animal)

    def displayActivity(self):
        print("观察每一种动物的活动方式：")
        for animal in self.__animals:
            animal.moving()

    def monkeyClimbing(self, monkey):
        monkey.climbing()


def testZoo():
    zoo = Zoo()
    zoo.addAnimal(TerrestrialAnimal("狗"))
    zoo.addAnimal(AquaticAnimal("鱼"))
    zoo.addAnimal(BirdAnimal("鸟"))
    monkey = Monkey("猴子")
    zoo.addAnimal(monkey)
    zoo.displayActivity()
    print()
    print("观察猴子的爬树行为：")
    zoo.monkeyClimbing(monkey)


testZoo()
"""
观察每一种动物的活动方式：
狗在陆上跑...
鱼在水里游...
鸟在天空飞...
猴子在陆上跑...

观察猴子的爬树行为：
猴子在爬树，动作灵活轻盈...
"""