class Gun:
    "枪类"
    def __init__(self, type):
        self.type = type
        self.isFull = False

    def __set_bullet__(self):
        self.isFull = True
        print("装填完毕")

    def fire(self):
        if self.isFull is True:
            print("砰")
        else:
            print("未装弹")
