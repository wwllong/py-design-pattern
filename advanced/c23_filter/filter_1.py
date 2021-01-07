# 过滤模式 - 制作一杯鲜纯细腻的豆浆
class FilterScreen:
    """过滤网"""

    def doFilter(self, rawMaterials):
        for material in rawMaterials:
            if (material == "豆渣"):
                rawMaterials.remove(material)
        return rawMaterials


def testFilterScreen():
    rawMaterials = ["豆浆", "豆渣"]
    print("过滤前：", rawMaterials)
    filter = FilterScreen()
    filteredMaterials = filter.doFilter(rawMaterials)
    print("过滤后：",filteredMaterials)


# 使用python自带过滤函数
def testFilter():
    rawMaterials = ["豆浆", "豆渣"]
    print("过滤前：", rawMaterials)
    filteredMaterials = list(filter(lambda material: material == "豆浆", rawMaterials))
    print("过滤后：", filteredMaterials)


if __name__ == '__main__':
    testFilterScreen()
    testFilter()

"""
过滤前： ['豆浆', '豆渣']
过滤后： ['豆浆']
过滤前： ['豆浆', '豆渣']
过滤后： ['豆浆']
"""