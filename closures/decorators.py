# # Decorator is basically a function that take another function as an argument,
# #add some kinds of functionality and returns "another" function!
# #all without changing the source code of the original fxn that is calling it

# def decorator_function(original_function):
#     def wrapper_function():
#         print(f'wrapper executed this before {original_function.__name__}')
#         return original_function()
#     return wrapper_function

# @decorator_function
# def display():
#     print('The display function ran!')

# display()#<-- cal original function

# # decorated_display = decorator_function(display)
# # decorated_display() #<--- now instead of doing this we can do 2decorator_function,
# #Hence the decorator @ comes from this functionality

# #Now this syntax shows error if we passed arguments from original function
# #i.e.

# @decorator_function
# def display_info(name,age):
#     print(f"display_info ran with arguments ({name},{age})")

# display_info('John',25) #<- THis gives error because our wrapper_function() is not designed to take any argument
# #Hence we use args and kwargs in wrapper function, now it becomes:


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):#<-- now it takes any arbitrary no of keyword arguments from fxn calls
        print(f'wrapper executed this before {original_function.__name__}')
        return original_function(*args,**kwargs)
    return wrapper_function

@decorator_function
def display():
    print('The display function ran!')

display()

@decorator_function
def display_info(name,age):
    print(f"display_info ran with arguments ({name},{age})")

display_info('John',25) 


#------ Using classes as decorator:

class DecoratorClass(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self,*args,**kwargs): # THe __call__() method is used instead of wrapper_function!!!
        print(f'call method executed this before {self.original_function.__name__}')
        return self.original_function(*args,**kwargs)

# Now using decorator class: 
@DecoratorClass
def display_class():
    print('The display function ran using decorator class!')

display_class()

@DecoratorClass
def display_info_class(name,age):
    print(f"display_info_class ran with arguments ({name},{age})")

display_info_class('Jane',22) 

