import time

def calculate_time(func):
    start_time = time.time()
    func()
    end_time = time.time()
    total_time = start_time - end_time
    X = str(int(total_time))
    print ('Total time ' + X)

