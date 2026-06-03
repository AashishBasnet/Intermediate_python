# so this decorator argument stuff is even 1 more level deep
def prefix_decorator(prefix):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):#<-- now it takes any arbitrary no of keyword arguments from fxn calls
            print(prefix, f'wrapper executed this before {original_function.__name__}')
            return original_function(*args,**kwargs)
            print(prefix, f'wrapper executed this after {original_function.__name__}')
        return wrapper_function
    return decorator_function



@prefix_decorator('Testing: ') #<--- now we have the testing prefix sent!
def display_info(name,age):
    print(f"display_info ran with arguments ({name},{age})")

display_info('John',25) 
display_info('Travis',30) 
# This is used in frameworks like flask!!!