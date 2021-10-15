import time

def calculate_time(func):
    start_time = time.time()
    func()
    end_time = time.time()
    total_time = end_time - start_time
    X = int(total_time)
    return ('Total time %s' %(X))

