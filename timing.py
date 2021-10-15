import time

def calculate_time(func):
    start_time = time.time()
    print(start_time)
    func()
    end_time = time.time()
    print(end_time)
    total_time = end_time - start_time
    X = int(total_time)
    s = 'Total time is ' + X
    return str(s)