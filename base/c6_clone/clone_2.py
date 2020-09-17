# 克隆宠物店，深拷贝和浅拷贝
from copy import copy, deepcopy


class PetStore:
    """宠物店"""

    def __init__(self, name):
        self.__name = name
        self.__petList = []

    def setName(self, name):
        self.__name = name

    def showMyself(self):
        print("%s 宠物店有以下宠物：" % self.__name)
        for pet in self.__petList:
            print(pet + "\t", end="")
        print()

    def addPet(self, pet):
        self.__petList.append(pet)


def testPetStore():
    petter = PetStore("Petter")
    petter.addPet("小狗Coco")
    print("父本petter：", end="")
    petter.showMyself()
    print()

    petter1 = deepcopy(petter)
    petter1.addPet("小猫Amy")
    print("副本petter1：", end="")
    petter1.showMyself()
    print("父本petter：", end="")
    petter.showMyself()
    print()

    petter2 = copy(petter)
    petter2.addPet("小兔Ricky")
    print("副本petter2：", end="")
    petter2.showMyself()
    print("父本petter：", end="")
    petter.showMyself()


if __name__ == "__main__":
    testPetStore()


'''
父本petter：Petter 宠物店有以下宠物：
小狗Coco	

副本petter1：Petter 宠物店有以下宠物：
小狗Coco	小猫Amy	
父本petter：Petter 宠物店有以下宠物：
小狗Coco	

副本petter2：Petter 宠物店有以下宠物：
小狗Coco	小兔Ricky	
父本petter：Petter 宠物店有以下宠物：
小狗Coco	小兔Ricky
'''