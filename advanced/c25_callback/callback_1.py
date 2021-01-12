# 回调机制 - 迎新大会,展示才能
class Employee:
    """公司员工"""

    def __init__(self, name):
        self.__name = name

    def doPerformance(self, skill):
        print(self.__name + "的表演:", end="")
        skill()


def sing():
    """唱歌"""
    print("唱一首歌")


def dling():
    """拉Ukulele"""
    print("拉一曲Ukulele")


def joke():
    """说段子"""
    print("说一搞笑段子")


def performMagicTricks():
    """表演魔术"""
    print("神秘魔术")


def skateboarding():
    """玩滑板"""
    print("酷炫滑板")


def testSkill():
    helen = Employee("Helen")
    helen.doPerformance(sing)
    frank = Employee("Frank")
    frank.doPerformance(dling)
    jacky = Employee("Jacky")
    jacky.doPerformance(joke)
    chork = Employee("Chork")
    chork.doPerformance(performMagicTricks)
    Kerry = Employee("Kerry")
    Kerry.doPerformance(skateboarding)


if __name__ == '__main__':
    testSkill()
"""
Helen的表演:唱一首歌
Frank的表演:拉一曲Ukulele
Jacky的表演:说一搞笑段子
Chork的表演:神秘魔术
Kerry的表演:酷炫滑板
"""