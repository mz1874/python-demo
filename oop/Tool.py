class Tool:
    # 类似静态变量
    number = None

    # 类似静态方法 但是对于类方法而言的话指的是 类方法涉及 对当前类属性的引用

    # 而对于 静态方法而言 它并不涉及
    @classmethod
    def who_am_i(cls):
       return cls.number

    # 静态方法 并没有引用当前的实例数据 或者类数据
    @staticmethod
    def print_hello():
        print("hello")


if __name__ == '__main__':
    #  静态方法和类方法都可以使用  类名.方法
    Tool.print_hello()
    print(Tool.who_am_i())
