import types
class Animal(object):
    def __init__(self,name):
        self.name = name
w = 100
dog = Animal('dog')

def eat(self):
    print('--%s在吃肉'%self.name)

def go(a):
    print('%sds'%a)

go('nihao 世界')
dog.eat = types.MethodType(eat, dog)

dog.eat()
