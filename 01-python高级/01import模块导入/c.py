class Parent(object):
    def say1(self):
      print('heelo')


class Child(Parent):
    def say(self):
      self.say1()

    def __del__(str):
      print('111')
    
    def __new__(cls):
      return super().__new__(cls)
      

  
a = Child()
# a.say()
# del a
