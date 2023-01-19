"""
python 中的变量

整数类型 number
布尔类型
浮点数
复数型


非数字型：

字符串
列表
元组
字典

在python 2.* 中同样存在 long

如果变量类型为 bool 那么在计算的时候 可以作为1 和 0
"""

index = True    # 默认等于1
second_index = False  # 默认等于0

print(index + 1)
print("两者的和是", (1 + second_index))


# 在Python 中并不需要主动去定义数据的类型, 因为 A = {表达式} Python 会根据表达式的类型推断 变量的类型

# 同时在Py中可以使用 type 查看 数据的类型
print(type(second_index))  #<class 'bool'>

number = int(True)

print(number)

float_number = float(index)

print(float_number)

# 可以使用对应的强制类型转换将一类类型转换为其他的另一种类型

# str int float bool 等

# 同时在python 中可以使用 input 来获取用户输入

user_name = input("请输入用户名\n")

user_password = input("请输入密码\n")

user_money = input("请输入你具有多少钱\n")

print(type(user_name))  #TODO 1 在这里而言 input 只能输入str类型
print("将钱的小数转换成 float ：", float(user_money))


# python 中使用格式化输出
print("%s has %f RMB " % (user_name, float(user_money)))

price = 9.9
weight = 80




## 主意 在格式化输出的时候如果  %.后表示 0 后面显示几位小数 如果是 浮点型的话则使用 f  字符串则是 s 整数则是D


print("我的名字叫 %s，请多多关照！" % user_name)
print("我的学号是 %06d" % int(user_password))
print("苹果单价 %.9f 元／斤，购买 %.2f 斤，需要支付 %.07f 元" % (price, weight, price * weight))
# print("数据比例是 %.02f%%" % (scale * 100))

