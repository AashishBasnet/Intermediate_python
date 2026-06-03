def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

my_nums = square_numbers([1,2,3,4,5])
print (my_nums) 
# To convert it into a generator, we do:

def sq_numbers(nums):
    for i in nums:
        yield(i*i)

my_nums = sq_numbers([1,2,3,4,5])
print (my_nums) #<-- returns generator object because generators don't hold entire result in memory
#so we do:
print(next(my_nums)) #generator only stores the current value it yeilds each value each time its called!
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
# There were 5 elements on the list so we called it 5 times
#but if there were more than 5 in list, we should have called as much as it has elements on list
# However, if you call it for more time than needed, it will cause error. Hence:
# print(next(my_nums)) #<--- This shows error

# Now to write it as list comprehension (easier):

my_nums = [x*x for x in [1,2,3,4,5]]

print (list(my_nums))
print (my_nums)


#<-- but a list has low performance. I.e. it takes more time
#hence we use a generator!!
#so you lose performance if you use list