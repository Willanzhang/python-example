class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    def setNewAge(self, newAge):
        if newAge > 0 and newAge <= 100:
            self.__age = newAge

    def __str__(self):
        return

    