#coding ='utf-8'
class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    def setNewAge(self, newAge):
        if newAge > 0 and newAge <= 100:
            self.__age = newAge

    def __str__(self):
        return '这里老王'

    def __del__(self):
        print('删除')
    
# laowang = Person('老王', 19)
# del laowang
# print(laowang)
Person.age = 19
print(Person.age)