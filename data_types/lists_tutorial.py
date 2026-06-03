# Python Lists — Bullet Point Notes

# A list stores multiple items in a single variable.

# Lists can store different data types together.

# Lists allow duplicate values.

# Access list items using indexing.

# Index 0 → first item
# Index 1 → second item

# Negative indexing accesses items from the end.

# -1 → last item
# -2 → second last item

# Use a for loop to iterate through a list.

# Use "in" to check if an item exists in a list.

# len(list) gives the number of elements.

# --------------------------------------------------

# List Modification Methods

# append() adds an item to the end of the list.

# insert(index, value) adds an item at a specific position.

# pop() removes and returns the last item.

# remove(value) removes a specific item.

# remove() does not return the removed item.

# clear() removes all elements from the list.

# clear() also returns None.

# --------------------------------------------------

# Reversing and Sorting

# reverse() reverses the list in-place.

# sort() sorts the original list permanently.

# sorted() creates a new sorted list without changing the original.

# Difference:
# sort() → modifies original list
# sorted() → returns a new sorted list

# --------------------------------------------------

# Useful List Tricks

# Create a list with repeated values.

# Concatenate (join) two lists using +.

# --------------------------------------------------

# List Slicing

# General syntax:
# list[start:end:step]

# Slice from index 1 to 3.

# From beginning to index 3.

# From index 2 to end.

# Skip alternate items using step.

# Reverse a list using slicing.

# --------------------------------------------------

# Copying Lists

# Direct assignment does not create a real copy.

# Both variables point to the same list.

# Modifying copied list also changes original list.

# Correct Ways to Copy a List

# Using .copy()

# Using list()

# Using slicing

# --------------------------------------------------

# List Comprehension

# Create a new list in a single line.

# Example:
# al = [1,2,3]
# bl = [1,4,9]

# Used for:
# transforming data
# filtering items
# cleaner and shorter code



mylist = ["banana","cherry",'apple']
print(mylist)

mylist2 = [5, True, 'apple','apple'] #list allows duplicates

item = mylist[0]
print(mylist2)
print(item) #prints banana if index = 0

#negative indexing:
item2 = mylist[-1]
print(item2) #prints last member of list if index = -1 and so on.

for i in mylist:
    print(i)

if "banana" in mylist:
    print ('yes')
else:
    print('no')

#to check no of elements:

print(len(mylist))

mylist.append('lemon') #adds new element at last of list
print(mylist)

mylist.insert(1,'blueberry') #insert however adds value to list at the index specified

print(mylist)

itemp = mylist.pop()# returns last item and also removes it

print(itemp)
print(mylist)

itemr = mylist.remove("cherry")

print(itemr) #Therefore the remove method does not return the item
print(mylist)

# Hence -- append and pop // insert and remove

#However while removing all items from list, use clear

itemc = mylist.clear()
print(itemc) #Therefore the clear method also does not return the item
print(mylist)


#again, taking a new list
my_list = ["banana","cherry",'apple']

# 1. Reverse

my_list.reverse()
print(my_list)



# 2. Sort

my_list.sort()
print(my_list)
num_list = [4,3,2,0,-1,9,7,8,-2]
print(num_list)

# 3. Sorted - creates new list
new_list = sorted(my_list)
print(my_list) # The old list remains same
print(new_list)# the sorted value is in new list

# Think of it this way: sort - to sort the list // sorted -  To create a new SORTED list

# Tricks: ---- 

# to make a list with 5 zeroes:

zero_list = [0] * 5
print(zero_list) # gives [0,0,0,0,0]

# concatenate 2 list

num_c_list = [1,2,3,4,5]

conc_list = num_c_list + my_list
print(conc_list) # concatenates both num_c_list and my_list to create a new list
conc_list2 =  my_list + num_c_list 
print(conc_list2) # concatenates both num_c_list and my_list to create a new list but here, reversed


#slicing

a = conc_list2[1:4] # from item 1 to 3 i.e less than 4 i.e. 1 is included not 4
print(a)


b = conc_list2[:4] # no start index means starts from first till 4
print(b)

c = conc_list2[2:] # no end index means starts from 2 till last
print(c)

d = conc_list2[1::2] # starts from 1 till last but step = 2 so skips alternate
print(d)

e = conc_list2[::2] # starts from 0 till last but step = 2 so skips alternate
print(e)


f = conc_list2[::-1] # reverses list
print(f)

g = conc_list2[::-2] # reverses list with 2 step alternate
print(g)


# copying a list

list_org = ['banana','cherry','apple']

list_cpy = list_org
print(f'original list: {list_org}') #this is org list
print(f'copy list: {list_cpy}') # this is the copy of the original list

# !!!!!!!!--- However : if you modify the COPY list, it also modifies original.

list_cpy.append('blueberry')
print(f'original list: {list_org}') #this is org list --which is also modified
print(f'copy list: {list_cpy}') # this is the copy of the original list

### TO make an actual copy however, you can use the .copy() method !!!!!!!!

list_cpy = list_org.copy()
print(f'original list: {list_org}') #this is org list
print(f'copy list: {list_cpy}') # this is the copy of the original list

# Now it can't change the org list ---------------
list_cpy.append('mango')
print(f'original list: {list_org}') #this is org list --which is not modified
print(f'copy list: {list_cpy}') # this is the copy of the original list


# can also use the list() function to make copy i.e.

list_cpy = list(list_org)
print(f'original list: {list_org}') #this is org list
print(f'copy list: {list_cpy}') # this is the copy of the original list

# can also use the slicing to make copy i.e.

list_cpy = list_org[:] #makes a slice i.e. all the way from beginning to end
print(f'original list: {list_org}') #this is org list
print(f'copy list: {list_cpy}') # this is the copy of the original list

#list comprehension ---make new list from last list in 1 line:

al = [1,2,3,4,5,6]
bl = [i*i for i in al]

print(al)
print(bl) # creates a list of squared elements of each element in list al


lister = [1,2,3,4,7,6,5]
lister.remove(2)
print(lister)