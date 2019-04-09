from multiprocessing import Queue,Process
from time import sleep
import random

def write(q):
    for x in ['A', 'B', 'C']:
        q.put(x)
        sleep(random.random())
        print('在queue中塞入%s'%x)

def read(q):
    while True:
        if not q.empty():
            x = q.get(True)
            sleep(random.random())
            print('读取数据%s'%x)
        else:
            break
    
q = Queue()

qw = Process(target=write, args=(q,))
qr = Process(target=read, args=(q,))

qw.start()
qw.join()

qr.start()
qr.join()