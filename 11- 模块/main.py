from 模块1 import title
from 模块1 import User
# 上述的方法为部分导入

# import 模块1 as a
# import 模块2 as b
#  上述的导入方法 导入了整个模块包括其中的类。用户可以使用 as 的方式来给导入的模块起一个别名
# 模块的别名需要满足大驼峰命名法  that 每个单词的首字母使用大写

# 局部导入
wang = User()
print(type (wang))


print(title)

# a.say_hello()
# b.say_hello()