import time

def calculate_time(func):
    '''
    Decorator function to calculate time it takes to run a function.
    '''
    def wrapper():
        '''
        Inner function to operate the decorator.
        '''
        start_time = time.time()
        func()
        end_time = time.time()
        total_time = end_time - start_time
        print (f'Total time {total_time}')
    return wrapper
    

