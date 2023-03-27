class User:
    def __init__(self):
        # 修饰作为私有属性 即使用户实例化也无法访问
        self.__age = 99

    def __haha(self):
        print("我是一个私有方法无法被外界调用")



if __name__ == '__main__':
    zhangsan = User()
    print (zhangsan._User__age)
    print(zhangsan._User__haha())

