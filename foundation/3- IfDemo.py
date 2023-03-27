import random

age = 2
sex = '女'

if age == 90 and sex == '女':
    print("正确")
elif age > 90:
    print("age > 90")
else:
    print("不在区间内")


## 石头剪刀布


userPointer = int(input("石头1 、剪刀2、布3"))


computerPointer = random.randint(1,3)

if userPointer == computerPointer:
    print("平局")
elif (userPointer == 1 and computerPointer == 2) \
        or (userPointer == 2 and computerPointer == 3)\
        or (userPointer == 3 and computerPointer == 1):
    print("恭喜你获胜了")
else:
    print("电脑获胜")
