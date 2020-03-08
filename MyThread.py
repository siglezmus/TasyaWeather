import threading
import time

from main import *

class MyThread(threading.Thread):
    def __init__(self):
        super().__init__(self)
    def start(self):
        self.run(self)
    def run(self):
        while True:
            time.sleep(20)
            # if((self.day != datetime.datetime.now().day) & (self.hour >= 6)):
            send_msg()