'''
Multithread:
Parellel/ Concurrent process:
'''

from threading import *

class Alpha(Thread):
    def __init__(self):
        super().__init__()
        print("Initiated")
    def run(self):
        print("access")
        self.check()
    def check(self):
        print("Check access")
        

a=Alpha()
a.start()