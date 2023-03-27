# * 列表 数组
# * 元组
# * 字典
# * 字符串
# * 公共方法
# * 变量高级

persons = ['张三', '李四', '王五', '马六', '张三']

number = [3, 1, 1, 1]

# 增加一个元素到结尾
persons.append('22')

# del persons[1]  尽量不要使用del 关键字 此关键词是直接操作内存地址进行删除

# 删除第一次出现的
persons.remove('张三')

# 根据指定的位置插入
persons.insert(0, '00')

# 添加一个数组到另一个数组
persons.extend(number)

# append在数组后增加数据
persons.append("我是在数组结尾增加的数据")

# pop 如果不传递参数的话则会默认移动最后一个
#  如果传递参数 的话则弹出一个元素
persons.pop()


# persons.sort(reverse=True) 排序  降序和升序

# 倒叙
persons.reverse()

for i in persons:
    print(i)
