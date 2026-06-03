#Dictionary: collection of key-value pairs, Unordered, Mutable
my_dict = {"name":"Aashish","age":22,"city":"Kathmandu"}
print(my_dict)

my_dict2 = dict(name ="Animesh",age="16", city = "Bhaktapur")
print(my_dict2)

value = my_dict['name']
print(value) #<---access item via key

my_dict['email'] = 'ahs@gmail.com'
print(my_dict)

# --- To delete items in dict

del my_dict2['age']
print(my_dict2)

#---or use pop method
my_dict.pop('city')
print(my_dict)


#---- to remove last item:
my_dict.popitem()
print(my_dict)

#----to see if the key is there

if "name" in my_dict:
    print(my_dict['name'])

# accessing sth not on list

try:
    print(my_dict['last_name'])
except:
    print('not found error')

#---------------- Looping in dict

for key in my_dict:
    print(key)

#or:

for key in my_dict.keys(): # <-only looks key in dict
    print(f'second: {key}')

for values in my_dict.values():
    print(values)


# or---

for key,value in my_dict.items(): #<-returns list of tuples
    print(key,value)

print(my_dict.items()) # <------List of Tuples

my_dict_cpy = my_dict #<--easy way to copy dict

print(my_dict_cpy)

# !However modifying the new will modify original

#so, use copy method
my_dict_cpy = my_dict.copy()

#or use dict fxn
my_dict_cpy = dict(my_dict)

#THESE WONT AFFECT ORG DICT

# TO update dict

my_dict_n1 = {"name":"Aashish","age": 21, "email":"ash@gmail.com"}
my_dict_n2 = {"name":"Animesh","age":16, "city":"kathmandu"}

my_dict_n1.update(my_dict_n2) #so it basically updates all the values of n1 to n2 and adds the key value pair that does not
#exist in n1

print(my_dict_n1)

#possible key types (can use numbers or tuples as key)
my_dict = {3:9,6:36,9:81}
print(my_dict)

value = my_dict[3]

print(value)

my_tuple = (8,7)

my_dict = {my_tuple: 15}

print(my_dict)

# my_list = [8,7] # !------------List cannot be used as key cuz its mutable and unhashable

# my_dict = {my_list: 15}

# print(my_dict)