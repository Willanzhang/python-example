# coding = 'urf-8'

class People(object):
    name = 'william'
    __age = '18'
    def __init__(slef):
        pass
    @classmethod
    def setNew(cls, newName):
        cls.name = newName
        print(cls)

    @staticmethod
    def oneF():
        print()

# a = People()
# print(a.name)
# People.setNew('')
# print(People.name)

# a.name = 'zbw'
# print(dir(People))
# print(People.__mro__)
People.oneF()
# People.go()