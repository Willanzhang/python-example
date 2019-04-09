from multiprocessing import Process
import time

class MyNewProcess(Process):
    def run(self):
        while True:
            print('this is child')
            time.sleep(1)
    def __init__(self):
