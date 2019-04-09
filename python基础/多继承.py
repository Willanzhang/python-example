class Ma(object):
    def run(self):
        print('------100km/h----跑')

class Lv(object):
    def run1(self):
        print('------900km/h----跑')


class Luozi(Ma, Lv):
    def __init__(self,name = '骡子'):
        self.name = name 

    def test(self):
        print(super().run1())


l = Luozi('小骡子')

l.test()
print(Luozi.__mro__)
