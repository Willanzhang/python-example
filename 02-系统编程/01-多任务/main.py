from ctypes import *
from threading import Thread

#加载动态库
lib = cdll.LoadLibrary('./libdeadloop.so')

#创建一个子线程，让其执行c语言编写得函数，此函数是一个死循环
t = Thread(target=lib.DeadLoop)
t.start()

#主线程，也调用c语言编写得那个死循环函数
#lib.DeadLoop()

while True:
    pass