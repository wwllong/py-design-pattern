# 依赖倒置原则，Dependence Inversion Principle
from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    """动物"""

    def __init__(self, name):
        self._name = name

    def eat(self, food):
        if(self.checkFood(food)):
            print(self._name + "进食" + food.getName())
        else:
            print(self._name + "不吃" + food.getName())

    @abstractmethod
    def checkFood(self, food):
        """检查哪种食物能吃"""
        pass


class Dog(Animal):
    """狗"""

    def __init__(self):
        super().__init__("狗")

    def checkFood(self, food):
        return food.category() == "肉类"


class Swallow(Animal):
    """燕子"""

    def __init__(self):
        super().__init__("燕子")

    def checkFood(self, food):
        return food.category() == "昆虫"


class Food(metaclass=ABCMeta):
    """食物"""

    def __init__(self, name):
        self._name = name

    def getName(self):
        return self._name

    @abstractmethod
    def category(self):
        """食物类别"""
        pass

    @abstractmethod
    def nutrient(self):
        """营养成分"""
        pass


class Meat(Food):
    """肉"""

    def __init__(self):
        super().__init__("肉")

    def category(self):
        return "肉类"

    def nutrient(self):
        return "蛋白质、脂肪"


class Worm(Food):
    """虫子"""

    def __init__(self):
        super().__init__("虫子")

    def category(self):
        return "昆虫"

    def nutrient(self):
        return "蛋白质含、微量元素"


def testFood():
    dog = Dog()
    swallow = Swallow()
    meat = Meat()
    worm = Worm()
    dog.eat(meat)
    dog.eat(worm)
    swallow.eat(meat)
    swallow.eat(worm)


testFood()

'''
狗进食肉
狗不吃虫子
燕子不吃肉
燕子进食虫子
'''
