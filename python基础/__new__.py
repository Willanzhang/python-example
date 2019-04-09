#coding = 'utf-8'

# class Old(object):
#     pass


# class New(Old):
#     def __init__(self):
#         print('this is init', self)

#     def __new__(cls):
#         print('this is new', cls)
#         return Old.__new__(cls)

# a = New()

class Singleton(object):
    __instance = None
    __first_init = False

    def __new__(cls, age, name):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance
    
    def __init__(self, age, name):
        pass

a = Singleton(12, 'william')
b = Singleton(18, 'william')
print(a)
print(b)