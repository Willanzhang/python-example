class Cat(object):
    def __init__(self, name, color ='白色'):
        self.name = name 
        print('11111', self.name)
        self.color = color 
    def __test(self):
        print('7777')
    def run(self):
        print('%s---在跑'%self.name)
    def get2(self):
        print('6666', self.name)

class Cat1(object):
    def __init__(self, name, color ='白色'):
        self.name = name 
        print('3333', self.name)
        self.color = color 
    
    def get1(self):
        print('5555', self.name)

    def run(self):
        print('%s---在跑'%self.name)


class Bosi(Cat1,Cat):
    # def __init__(self, name, color ='白色'):
    #     self.name = name 
    #     print('22222', self.name)
    #     self.color = color 

    def setNewName(self, newName):
        self.name = newName

    def test(self):
        # self.__test()
        self.get1()

    def getName(self):
        return self.name

    def eat(self):
        print('%s-----在吃东西'%self.name)


mao = Bosi('波斯猫')
mao.run()
print(mao.getName())
mao.get1()
mao.get2()
mao.test()