# 过滤模式应用 - 信息发布敏感词过滤

import re
# 引入正则表达式库
from filter_frame import Filter, FilterChain


class SensitiveFilter(Filter):
    """敏感词过滤"""

    def __init__(self):
        self.__sensitives = ["黄色", "台独", "贪污"]

    def doFilter(self, elements):
        # 敏感词列表转换成正则表达式
        regex = ""
        for word in self.__sensitives:
            regex += word + "|"
        regex = regex[0: len(regex) - 1]

        # 对每个元素进行过滤
        newElements = []
        for element in elements:
            item, num = re.subn(regex, "", element)
            newElements.append(item)

        return newElements


class HtmlFilter(Filter):
    """HTML特殊字符转换"""

    def __init__(self):
        self.__wordMap = {
            "&": "&amp;",
            "'": " &apos;",
            ">": "&gt;",
            "<": "&lt;",
            "\"": " &quot;",
        }

    def doFilter(self, elements):
        newElements = []
        for element in elements:
            for key, value in self.__wordMap.items():
                element = element.replace(key, value)
            newElements.append(element)
        return newElements


def testFilterContent():
    contents = [
        '有人出售黄色书：<黄情味道>',
        '有人企图搞台独活动, ——"造谣咨询"',
    ]
    print("过滤前的内容：", contents)
    filterChain = FilterChain()
    filterChain.addFilter(SensitiveFilter())
    filterChain.addFilter(HtmlFilter())
    newContents = filterChain.doFilter(contents)
    print("过滤后的内容：", newContents)


if __name__ == '__main__':
    testFilterContent()

"""
过滤前的内容： ['有人出售黄色书：<黄情味道>', '有人企图搞台独活动, ——"造谣咨询"']
过滤后的内容： ['有人出售书：&lt;黄情味道&gt;', '有人企图搞活动, —— &quot;造谣咨询 &quot;']
"""