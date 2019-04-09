#coding = 'utf-8'

class Class(object):
    name = 'william'
    def run(self):
        print('runing', name)
    def __init__(self):
        self.age = 1
        # name += 1
        # self.name = 'zbw'
        print(self.name)

    def __del__(self):
        print('000')

zbw = Class()
# del zbw
print(Class.name)