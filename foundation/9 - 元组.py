info_tuple = ("zhangsan", 18, 1.75, 1, 2, 3, 44, 44, 2, 1, 3)

# 元组的定义是使用（） 在当前的元组中如果这个元组只存在一个元素那么这个元素后面需要加， 进行分割
number = (2,)
for i in info_tuple:
    print(i)

# 使用len 来确定元组的长度
print(len(info_tuple))

print("元组中出现数据的次数", info_tuple.count(1))

userInfo = ('zhangsan', 19)
print("我的名字是 %s  我的年龄是 %d" % userInfo)

# 同时使用 list() 可以将元组转换成列表
print("开始将list 转换成列表" + "*" * 99)
arr = list(info_tuple)

print(type(arr))

for i in arr:
    print(i)

helloWorld = {'name': 'zhang', 'age': 12, "sex": 'nan', "address": "ss15"}

print(helloWorld.get("name"))

print(helloWorld.setdefault("money", 99))

# 列表 输出所有的 key 和 v
print(helloWorld.items())

# 删除一个k-v 如果k 不存在则会报错
helloWorld.pop("name")

# 列表 输出所有的 key 和 v
print(helloWorld.items())

# 清空当前的字典
# helloWorld.clear();

# print(helloWorld.items())


# 创建新的字典
# print(helloWorld.fromkeys(helloWorld.keys(),"11"))

# 随机弹出Key
# helloWorld.popitem()

# 输出k-v 中所有的v
print(helloWorld.values())

print(helloWorld.values())


#  将另一个子弹增加到这个里面
helloWorld.update()
