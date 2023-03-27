from oop.Animals import Animals



class Dog(Animals):

    def __str__(self):
     super(Dog, self).__str__()
     return "我是子类"
        # return "是我"


if __name__ == '__main__':
    pet1 = Dog()
    pet2= Dog()

    """
        这里有一个非常有趣的问题
    
    """
    pet1.age = 1
    pet2.age = 9

    Dog.age = 2

    print(pet1.age)
    print(pet2.age)

