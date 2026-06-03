my_tuple = ("max",28,"Boston")
print(my_tuple)

#------- Tuple only takes more than 1 object so

my_tuple = ("max") # <--- This is not a tuple but only string "str"
print(type(my_tuple)) 

my_tuple = ("max",) # <--- However it works after a comma though
print(type(my_tuple)) 

my_tuple = tuple(["max",28,"Boston"]) #<- can also make tuple from list
print(my_tuple)

item = my_tuple[0]
print(item)

#my_tuple[0] = "Tim" # <---- causes error cuz tuple is immutable

for i in my_tuple:
    print(i)

if "max" in my_tuple:
    print('yes')
else:
    print('no')

my_tuple = ('a','p','p','l','e')

print(len(my_tuple))

print(my_tuple.count('p')) 
print(my_tuple.index('p')) #<-- gives index of only first p value @ tuple

my_list = list(my_tuple) # <--- can change tuple to list
print(my_list)


my_tuple2 = tuple(my_list) #<----can change list back to tuple again
print(my_tuple2)

###------------ TUPLE slicing

a = (1,2,3,4,5,6,7,8,9,10)
b = a[:4]
c = a[2:5]
d = a[3:]
e = a[::2]
f = a[::-1]
print(b,c,d,e,f)

#------------ TUPLE unpacking

my_tuple = "Max",28,"Boston" ####<- can also define tuple without any braces, or anything w/o braces becomes tuple!!
print(my_tuple)

name,age,city = my_tuple #< --- tuple unpacking - object Must match the value inside the tuple
print(name)
print(age)
print(city)


####------ can also unpack this way
my_tuple3 = [1,2,3,4,5,6,7,8,9]
i1,*i2, i3 = my_tuple3 #<--since, i2 has that * in it, it gives a list and i1 and i3 give 1st and last element of tuple

print(i1)
print(i2)
print(i3)

## working with tuple can be efficient sometimes, specially while working with large data


#######################

import sys
my_list = [0,1,2,'hello', True]
my_tuple = (0,1,2,'hello',True)
print(f'List size: {sys.getsizeof(my_list)}bytes')
print(f'Tuple size: {sys.getsizeof(my_tuple)}bytes')

# CONCLUSION: even if both list and tuple have same elements, list is larger
# ----------> Hence making tuple lightweight and easier to iterate and create


#--------------------
import timeit
print(f'time taken for list: {timeit.timeit(stmt="[0,1,2,3,4,5]", number = 1000000)}')
print(f'time taken for tuple: {timeit.timeit(stmt="(0,1,2,3,4,5)", number = 1000000)}')


#CONCLUSION: ------ Tuple requires less time to be created than lists.... So working with tuple = more efficient