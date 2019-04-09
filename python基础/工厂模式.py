# coding= 'utf-8'

class Cake(object):
    def __init__(self):
        pass
    
    def weidao(self):
        print('好吃')

    def calorie(self):
        print('热量很高')

class CreamCake(Cake):
    
    def __init__(self):
        print('this is 奶油蛋糕')


class ChocolateCake(Cake):
    
    def __init__(self):
        print('this is 巧克力蛋糕')
    

class CakeFactory(object):
    def getCake(self,type):
        if type == '奶油蛋糕':
            self.cakeType = CreamCake()
        elif type == '巧克力蛋糕':
            self.cakeType = ChocolateCake()
        return self.cakeType

class CakeStore(object):

    def __init__(self):
        self.type = CakeFactory()

    def createOrder(self, type):
        self.cake  = self.type.getCake(type)
        self.cake.weidao()
        self.cake.calorie()

xi = CakeStore()
xi.createOrder('巧克力蛋糕')