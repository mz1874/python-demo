import sys

person_cards = []

operation_number = 0

def switch(number):
    if number == '1':
        user_name = input("输入姓名")
        print(type(user_name))
        age = input("age")
        print(type(age))
        person = {'name': user_name, 'age': age}
        print(type(person))
        person_cards.append(person)
        print("新增完成")
        main_menu()
        pass
    elif number == '2':
        for i in person_cards:
            print("name %s  \t age %s" % ((i.get("name")) ,i.get('age')))
        main_menu()
        pass
    elif number == '3':
        editName = input("请输入你要修改的Namw")
        for i in person_cards:
           oldName = i.get("name");
           if oldName != '' and oldName != None:
                newName = input("输入新名字")
                i['name'] = newName
                main_menu()

    else:
        print("系统退出")
        pass
def main_menu():
    print("*" * 100)
    print("欢迎使用文件管理系统")
    print("1 新建名片")
    print("2 显示全部")
    print("3 修改名片")
    print("4 退出")
    print("*" * 100)
    try:
        operation_number = input("请输入数字")
    except RuntimeError:
        print(sys.exc_info())
    else:
        print("我被执行")
    finally:
        print("最终")
    switch(operation_number)









if __name__ == '__main__':
    main_menu()
