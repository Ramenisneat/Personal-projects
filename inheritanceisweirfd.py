import time

def timer(f):
    def wrapper():
        start = time.time()
        f()
        total = time.time()-start
        print(total)
    return wrapper

@timer
def yes():
    for i in range(10000000):
        pass

yes()