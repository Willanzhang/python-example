#encoding=utf-8
import threading
from time import sleep

local_school = threading.local()

def process_student():
    student = local_school.student
    print('hello ,%s*in %s)'%(student, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    if name == '⽼王':
        print(name)
        sleep(2)
    process_student()

t1 = threading.Thread(target= process_thread, args=('dongGe',), name='Thread-Ass')
t2 = threading.Thread(target= process_thread, args=('⽼王',), name='Thread-Bss')
t1.start()
t2.start()
t1.join()
t2.join()
