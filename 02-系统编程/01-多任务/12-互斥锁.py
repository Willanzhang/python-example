# coding=utf-8
import threading
import time
g_num = 100

def work1():
    global g_num
    for i in range(10000000):
        mutex.acquire()
        g_num += 1
        mutex.release()
    
    print('____in work1 g_num = %d'%g_num)

def work2():
    global g_num
    for i in range(10000000):
        mutex.acquire()
        g_num += 1  
        mutex.release()

    print('____in work2 g_num = %d'%g_num)


print('____创建线程之前 g_num = %d'%g_num)

mutex = threading.Lock()

thread = threading.Thread(target=work1)
thread1 = threading.Thread(target=work2)

thread.start()
# time.sleep(1)

thread1.start()

print('____创建线程之后 g_num = %d'%g_num)
