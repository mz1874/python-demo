from oop.Gun import Gun


class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self):
        if self.gun is None:
            print("士兵没有枪， 无法开火")
        else:
            print("冲啊！！！")
            self.gun.__set_bullet__()
            self.gun.fire()
    def __addGun__(self, gun):
        self.gun = gun

if __name__ == '__main__':
    zhangSan = Soldier("张三")
    ak47 = Gun("ak47")
    zhangSan.__addGun__(ak47)
    zhangSan.fire()