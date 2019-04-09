import os
from multiprocessing import Process

def test(name):
    print('this is test')


p = Process(target=test, args=('test',))

p.start()

