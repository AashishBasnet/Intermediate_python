#In programming languages, a closure, also lexical closure or function closure,
#  is a technique for implementing lexically scoped name binding in a language with first-class functions.

def outer_func(msg):
    message = msg
    def inner_func():
        print(message)

    return inner_func #<-- this doesn't execute inner func but returns it

my_func = outer_func('Hi')
hello_func = outer_func('Hello!')
print(my_func.__name__) #<_-- since the outer func returns inner func, 
#The my_func variable becomes inner func! 
# Now, we can execute the inner func using my_func

my_func()
hello_func()
# To remember this just think: a closure closes over a free
#variable from the environment. In this case msg = free variable
