from threading import *

import _thread

def current(skill="c"):
    if skill == 'java':print(skill,"Opennings in Spring")
    elif skill == 'python':print(skill,"Opennings in Flask")
    elif skill == 'javascript':print(skill,"Opennings in React")
    else:print("No opennings in",skill)

t1=_thread.start_new_thread(current,('c',))
