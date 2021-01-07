# 过滤模式 - 制作一杯鲜纯细腻的豆浆,基于框架
from filter_frame import Filter


class FilterScreen(Filter):
    """过滤网"""

    def doFilter(self, elements):
        for material in elements:
            if (material == "豆渣"):
                elements.remove(material)
        return elements



def testFilterScreen():
    rawMaterials = ["豆浆", "豆渣"]
    print("过滤前：", rawMaterials)
    filter = FilterScreen()
    filteredMaterials = filter.doFilter(rawMaterials)
    print("过滤后：",filteredMaterials)


if __name__ == '__main__':
    testFilterScreen()

"""
过滤前： ['豆浆', '豆渣']
过滤后： ['豆浆']
"""
