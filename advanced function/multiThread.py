# coding=utf-8
# __author__ = "Peng Jidong"
# multi threading versions

from functools import wraps
import time
import threading
from concurrent.futures import thread
from AutoEvaluateTeach import EvaluateTeach

# aim to write a decorator to show how many time used
def time_use(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        print('[+] Starting counting time with function: %s' % (func.__name__))
        func(*args, **kwargs)
        end = time.time()
        print('[+] Ending counting with function: %s' % (func.__name__))
        print('[+] %s time use is: %s' % (func.__name__, end-start))
    return wrapper


@time_use
def foo():
    time.sleep(3)


@time_use
def ml():
    for i in range(5):
        a = EvaluateTeach('2201503184', 'pjd19970404')
        t = threading.Thread(target=a.run)
        t.start()
        t.join()


ml()
