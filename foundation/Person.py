class Person:
    "人类"

    def information(self):
        name = self.name
        age = self.age
        address = self.address
        print(type(age))
        print("name %s \t age %s \t address %s \t" % (name, age, address))

    def count(self, number, number2):  # 计算 A + b
        return number + number2
        pass

    "对象初始化时"
    def __init__(self):
        self.name = ''
        self.age = -1
        self.address = ''
        pass


    def __delete__(self, instance):
        print(instance)
        print("1")

    def __str__(self):
        return "class Person use for create person"

    "在对象被创建时"
    # def __new__(cls, *args, **kwargs):
        # print(cls)
        # print(args)
        # print(kwargs)



if __name__ == '__main__':
    # 创建对象
    wangChong = Person()
    wangChong.name = 'wang'
    wangChong.age = 19,
    wangChong.address = 'ss15'
    wangChong.information();
    print(wangChong)

    # 主意  虽然在py中 对象的属性可以通过外部定义的方式进行定义 但是最好不要使用这种方式 因为一旦外部定义
    # 在外部没有对类内的变量赋值的时候而调用了具有其引用的方法时会出现错误
#     通常根据类的生命周期进行类属性的初始化
