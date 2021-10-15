def tripler(func):
    '''
    This function calls the func function three times. Hence, tripler.
    '''
    def wrapper():
        func()
        func()
        func()
        
    return wrapper