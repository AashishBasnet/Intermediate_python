# First-Class Functions:
# "A programming language is said to have first-class functions if it treats functions as first-class citizens."

# First-Class Citizen (Object):
# "An entity which supports all the operations generally available to other entities.
#  These operations typically include being passed as an argument,
#  returned from a function, and assigned to a variable."

# We should be able to treat functions like any other variable or object

def square(x):
    return x * x

f = square(5)

print(square)
print(f)

#we can also do:
f = square #<--- now we did not only passed the return value of the function to the
#variable but we passed the entire function

print(square)
print(f)#<--so this gives same answer as the print(square) because they are same

#Hence, we can also do this:
print(f(5)) #<-- and now we used the variable as a function! i.e a variable converted as
#a function!!!!!

#now, passing a function as an argument to another function
def square(x):
    return x * x 

def my_map(func,arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map (square,[1,2,3,4,5])
print(squares)

#How to return a fxn from another fxn

def logger(msg):
    def log_message():
        print('Log',msg)
    return log_message

log_hi = logger('HI')
log_hi() #<-- parenthesis because we can now use this veriable as the log_message() function
# This is called closure

def html_tag(tag):
    def wrap_text(msg):
        print(f'<{tag}>{msg}</{tag}>')
    return wrap_text
print_h1 = html_tag('h1') #<-- first initialize the variable as original function
print_h1('Test headline') #<-- Now use the variable as function to call the inner function
print_h1('Another headline') 