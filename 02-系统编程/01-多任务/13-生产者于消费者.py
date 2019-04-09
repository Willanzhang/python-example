#encoding=utf-8
from threading
import time
from queue import Queue

class Producer(threading.Thread):
    def run(self):
        global queue