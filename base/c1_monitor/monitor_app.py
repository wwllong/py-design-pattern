# 监听模式应用-监控用户登陆

from monitor_frame import Observable, Observer
import time


# 导入时间处理模块

class Account(Observable):
    """用户账户"""

    def __init__(self):
        super().__init__()
        self.__latestIp = {}  # 最后一次登陆的IP
        self.__latestRegion = {}  # 最后一次登陆的地区

    def login(self, name, ip, time):
        region = self.__getRegion(ip)
        if self.__isLongDistance(name, region):
            self.notifyObserver({"name": name, "ip": ip, "region": region, "time": time})
        self.__latestRegion[name] = region
        self.__latestIp[name] = ip

    def __getRegion(self, ip):
        # 由IP地址获取地区信息。这里只是模拟，真实项目中应该调用IP地址解析服务
        ipRegions = {
            "101.47.18.9": "浙江省杭州市",
            "67.218.147.69": "美国洛杉矶",
            "113.108.182.52": "广东省广州市",
        }
        region = ipRegions.get(ip)
        return "" if region is None else region

    def __isLongDistance(self, name, region):
        # 计算本次登录与最近几次登录的地区差距。
        # 这里只是简单地用字符串匹配来模拟，真实的项目中应该调用地理信息相关的服务
        latestRegion = self.__latestRegion.get(name)
        return latestRegion is not None and latestRegion != region


class SmsSender(Observer):
    """短信发送器"""

    def update(self, observable, object):
        print("[短信发送] " + object["name"] + "您好！检测到您的账户可能登录异常。最近一次登录信息：\n"
              + "登录地区：" + object["region"] + "  登录ip：" + object["ip"] + "  登录时间："
              + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(object["time"])))


class MailSender(Observer):
    """邮件发送器"""

    def update(self, observable, object):
        print("[邮件发送] " + object["name"] + "您好！检测到您的账户可能登录异常。最近一次登录信息：\n"
              + "登录地区：" + object["region"] + "  登录ip：" + object["ip"] + "  登录时间："
              + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(object["time"])))


def testLogin():
    account = Account()
    account.addObserver(SmsSender())
    account.addObserver(MailSender())
    account.login("Jack", "101.47.18.9", time.time())
    account.login("Jack", "67.218.147.69", time.time())
    account.login("Jack", "113.108.182.52", time.time())
    account.login("Jack", "113.108.182.52", time.time())


def testTime():
    print(time.time())
    strTime = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.time()))
    print(strTime)


if __name__ == "__main__":
    testLogin()
    # testTime()

"""
[短信发送] Jack您好！检测到您的账户可能登录异常。最近一次登录信息：
登录地区：美国洛杉矶  登录ip：67.218.147.69  登录时间：2019-09-22 15:32:13
[邮件发送] Jack您好！检测到您的账户可能登录异常。最近一次登录信息：
登录地区：美国洛杉矶  登录ip：67.218.147.69  登录时间：2019-09-22 15:32:13
[短信发送] Jack您好！检测到您的账户可能登录异常。最近一次登录信息：
登录地区：广东省广州市  登录ip：113.108.182.52  登录时间：2019-09-22 15:32:13
[邮件发送] Jack您好！检测到您的账户可能登录异常。最近一次登录信息：
登录地区：广东省广州市  登录ip：113.108.182.52  登录时间：2019-09-22 15:32:13
"""