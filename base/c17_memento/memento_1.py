# 备忘录模式 - 好记性不如烂笔头


class Engineer:
    """工程师"""

    def __init__(self, name):
        self.__name = name
        self.__workItems = []

    def addWorkItem(self, item):
        self.__workItems.append(item)

    def forget(self):
        self.__workItems.clear()
        print(self.__name + "工作太忙了，都忘记要做什么了！")

    def writeTodoList(self):
        """将工作项记录到TodoList"""
        todoList = TodoList()
        for item in self.__workItems:
            todoList.writeWorkItem(item)
        return todoList

    def retrospect(self, todoList):
        """回忆工作项"""
        self.__workItems = todoList.getWorkItems()
        print(self.__name + "想起要做什么了！")

    def showWorkItem(self):
        if(len(self.__workItems)):
            print(self.__name + "的工作项：")
            for idx in range(0, len(self.__workItems)):
                print(str(idx + 1) + ". " + self.__workItems[idx] + ";")
        else:
            print(self.__name + "暂无工作项")


class TodoList:
    """工作项"""

    def __init__(self):
        self.__workItems = []

    def writeWorkItem(self, item):
        self.__workItems.append(item)

    def getWorkItems(self):
        return self.__workItems


class TodoListCaretaker:
    """TodoList管理类"""

    def __init__(self):
        self.__todoList = None

    def setTodoList(self, todoList):
        self.__todoList = todoList

    def getTodoList(self):
        return self.__todoList


def testEngineer():
    tony = Engineer("Tony")
    tony.addWorkItem("解决线上部分用户因为昵称过长而无法显示全的问题")
    tony.addWorkItem("完成PDF的解析")
    tony.addWorkItem("在阅读器中显示PDF第一页的内容")
    tony.showWorkItem()

    caretaker = TodoListCaretaker()
    caretaker.setTodoList(tony.writeTodoList())

    print()
    tony.forget()
    tony.showWorkItem()

    print()
    tony.retrospect(caretaker.getTodoList())
    tony.showWorkItem()


if __name__ == '__main__':
    testEngineer()

"""
Tony的工作项：
1. 解决线上部分用户因为昵称过长而无法显示全的问题;
2. 完成PDF的解析;
3. 在阅读器中显示PDF第一页的内容;

Tony工作太忙了，都忘记要做什么了！
Tony暂无工作项

Tony想起要做什么了！
Tony的工作项：
1. 解决线上部分用户因为昵称过长而无法显示全的问题;
2. 完成PDF的解析;
3. 在阅读器中显示PDF第一页的内容;

"""