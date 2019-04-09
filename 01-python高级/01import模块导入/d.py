class NewOj(object):
    def __init__(self, num):
        self.__num = num
    
    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, num):
        self.__num = num
    
    
t = NewOj(100)

print(t.num)


t.num = 200

print(t.num)