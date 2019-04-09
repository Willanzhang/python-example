# coding="utf-8"
# 枪类
class Gun:
    def __init__(self, danjiashuliang):
        self.danjiaList = None
        self.danjiashuliang = 1
    def andanjia(self, danjia):
        self.danjiaList = danjia
    def __str__(self):
        if not self.danjiaList:
            return '当前弹夹数量为1'   
        else:
            return ''  
    def she(self,diren):
        zidan = self.danjiaList.chuzidan()
        if zidan:
            zidan.shanghai(diren)

class Ak47(Gun):
    pass
class Sandan(Gun):
    def she(self,diren):
        i = 0
        while i < 3:
            zidan = self.danjiaList.chuzidan()
            i += 1
            if zidan:
                zidan.shanghai(diren)
            else:
                print('打了空枪')
# 子弹类
class Shot:
    def __init__(self, shashangli):
        self.shashangli = shashangli
        print('创建一颗子弹')
    def shanghai(self, diren):
        print('子弹')
        diren.diaoxue(self.shashangli)

# 弹夹
class Clip:
    def __init__(self, rongliang):
        self.rongliang = rongliang
        self.rongnaList = []

    def __str__(self):
        return '弹夹当前的子弹数量为:%d/%d'%(len(self.rongnaList),self.rongliang)

    def baocunzidan(self, zidan):
        if len(self.rongnaList) < self.rongliang:
            self.rongnaList.append(zidan)
    def chuzidan(self):
        if len(self.rongnaList) > 0:
            zidan = self.rongnaList[-1]
            self.rongnaList.pop()
            return zidan
        else:
            return None
# 人类
class Person:
    def __init__(self, name):
        self.name = name 
        self.xue = 100 
        self.gun = None
    def anzidan(self, danjia, zidan):
        danjia.baocunzidan(zidan)
    def andanjia(self, gun, danjia):
        gun.andanjia(danjia)
    def equip(self, gun):
        self.gun = gun
    def kaiqiang(self, diren):
        self.gun.she(diren)
    def diaoxue(self, shanghai):
        if self.xue < shanghai:
            print('%s已经挂了'%self.name)
        else:
            self.xue -= shanghai
            print(self.name,'当前生命值还有', self.xue)


laowang = Person('老王')
diren = Person('BOSS')
danjia = Clip(20)

gun = Sandan(1)

i = 0
while i < 5:
    zidan = Shot(5)
    laowang.anzidan(danjia,zidan)
    i += 1
laowang.andanjia(gun,danjia)
laowang.equip(gun)
laowang.kaiqiang(diren)
laowang.kaiqiang(diren)
print(danjia)
print(gun)