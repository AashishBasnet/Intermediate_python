# ordered and immutable data type in python with text representation

my_string = "Hello World" #can also use ''
print(my_string)

st2 = '''Hello, How are you!
Are you fine?'''
print(st2)

my_str = "Hello World"

my_char = my_string[0]
my_char2 = my_string[-1]

print(my_char)
print(my_char2)

substring = my_string[1:5]
substring2 = my_string[6:]
substring3 = my_string[:7]
substring4 = my_string[::-1]

print(substring)
print(substring2)
print(substring3)
print(substring4)

#------------String concatenation

my_str2 = "... How are you?"
print(my_str + my_str2)

for i in my_str2:
    print(i)

if 're' in my_str2:
    print('yes')
else:
    print('no')


my_string = "    Hello World   "
print(my_string)
my_string = my_string.strip() #have to assign to change string
print(my_string)
print(my_string.upper())
print(my_string.lower())
print(my_string.startswith('Hello'))
print(my_string.endswith('World'))
lst = my_string.lower()
print(lst.capitalize())
print(my_string.find('rld')) #<- returns index from where the string starts
print(my_string.count('o'))
print(my_string.replace('World','Universe'))


#------------LISTS and STRINGS

my_string = 'How are You, Doing'

my_list = my_string.split() #<---makes every word into list items. Because here space is the deli meter 
print(my_list)
my_list = my_string.split(',')
print(my_list)
my_string = ''.join(my_list)#<- joins every element in list with the string it is given to join with and changes it to string
print(my_string)

# ---THEREFORE--- split = string to list and '.join' = list to string

my_list = ['a'] *6 
print(my_list)


#---------We use JOIN and SPLIT because
#-----This operation commonly used is actually very expensive:
#---Hence BAD CODE:
my_string = ''

for i in my_list:
    my_string == i
print(my_string)


#GOOD METHOD:
my_string = ''.join(my_list)
print(my_string)


#IF you time check the JOIN method is way faster

#for string printing you can use % method or format or f-strings method

var = 'APPLE'

my_string = 'the variable is %s' % var
print(my_string)

var = 10

my_string = 'the variable is %d' % var
print(my_string)


var = 10.3333333

my_string = 'the variable is %.2f' % var
print(my_string)



var = 10.3333333
var2 = 3.9999999
my_string = 'the variable is {:.3f} and {:.4f}'.format(var,var2)
print(my_string)

var = 10.3333333
var2 = 3.9999999
my_string = f'the variable is {var*5:.2f} and {var2:.4f}'
print(my_string)