
import functools

def decorator_func(func):
    # @functools.wraps(func)
    def wrapper_message(*args,**kwargs):
        print("BEFORE_")
        # func(*args)
        print("AFTER_")
        return func(*args)
    
    return wrapper_message