# 外观/门面模式 - 新生报到
class Register:
    """报到登记"""

    def register(self, name):
        print("活动中心：%s 同学报到成功！" % name)


class Payment:
    """缴费中心"""

    def pay(self, name, money):
        print("缴费中心：收到 %s 同学 %s 元付款，缴费成功！" % (name, money))


class DormitoryManagementCenter:
    """宿舍管理中心"""

    def provideLivingGoods(self, name):
        print("生活中心：%s 同学的生活用品已发放。" % name)


class Dormitory:
    """宿舍"""

    def meetRoommate(self, name):
        print("宿舍 ：大家好！这是刚来的%s 同学，是你们未来需要共度四年的室友！相互认识一下...balala" % name)


class Volunteer:
    """迎新志愿者"""

    def __init__(self, name):
        self.__name = name
        self.__register = Register()
        self.payment = Payment()
        self.lifeCenter = DormitoryManagementCenter()
        self.__dormitory = Dormitory()

    def welcomeFreshmen(self, name):
        print("你好，%s 同学! 我是新生报到的志愿者%s ，我将带你完成整个报到流程。" % (name, self.__name))
        self.__register.register(name)
        self.payment.pay(name, 10000)
        self.lifeCenter.provideLivingGoods(name)
        self.__dormitory.meetRoommate(name)


def testRegister():
    volunteer = Volunteer("Frank")
    volunteer.welcomeFreshmen("Tony")


if __name__ == '__main__':
    testRegister()

"""
你好，Tony 同学! 我是新生报到的志愿者Frank ，我将带你完成整个报到流程。
活动中心：Tony 同学报到成功！
缴费中心：收到 Tony 同学 10000 元付款，缴费成功！
生活中心：Tony 同学的生活用品已发放。
宿舍 ：大家好！这是刚来的Tony 同学，是你们未来需要共度四年的室友！相互认识一下...balala
"""
