from oop.Item import Item


class Home:
    "家类"

    def __init__(self, name, area):
        self.name = name
        self.area = area
        self.items = []

    def __str__(self) -> str:
        str = ''
        for i in self.items:
            str += "\t" + i.name
        return "name %s size %d items %s " % (self.name, self.area, str)

    def addItem(self, item):
        if(self.area - item.size >= 0):
            self.items.append(item)
            print("添加成功")
            self.area -= item.size
        else:
            print("面积不足添加失败")



if __name__ == '__main__':
    myhome = Home("我的家", 99)
    bed = Item("床",2)
    table = Item("桌子",333)
    window = Item("窗户",2)
    myhome.addItem(bed)
    myhome.addItem(table)
    myhome.addItem(window)
    print(myhome.__str__())
