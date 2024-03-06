import inspect


def custom_reduce(func, iterable):
    args_count = len(inspect.getfullargspec(func).args)
    
    accumulator = iterable[0]
    
    for i in range(1, len(iterable), args_count - 1):
        pass
    
custom_reduce(lambda x, y: x * y, [1, 2, 3])    
    