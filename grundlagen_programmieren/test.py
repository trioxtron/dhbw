import time

def tictoc(func):
    def wrapper():
        t1 = time.time()
        func()
        t = time.time() - t1
        print(f"It took {t}s")
    return wrapper

@tictoc
def test():
    time.sleep(2)

test()
