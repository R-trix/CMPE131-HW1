import time

def calculate_time(func):
    start_time = time.time()
    func()
    end_time = time.time()
    print("Total time " + (start_time - end_time))
    

time.sleep(2)

