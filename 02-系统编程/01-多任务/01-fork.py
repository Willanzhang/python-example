import os
import time

ret= os.fork()

while True:
    time.sleep(1)
    print(ret)