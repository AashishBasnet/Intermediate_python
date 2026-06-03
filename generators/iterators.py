#Iterators and iterables
#iterable: Something that can be looped over eg. a list

nums = [1,2,3] #<--list
for num in nums:#<--list being looped over
    print(num)
# but what's going on inside it?
#How to know if its iterable?
# sth is iterable if it has .__iter__() dunder function!

print(dir(nums)) #<-- THis gives list of method the variable is allowed
# our list here has __iter__ hence it is an iterable
# SO what the for loop is doing on the background is calling __iter__ on our object and returning
#an iterator that we can loop over. Hence list is iterable
#But not an iterator!!
# But if we run __iter__() on list THEN, it returns an iterator
# SO what makes an iterator? 
#iterator == an object with a state so it remembers where it is during iteration!!
# an iterable like a list does not do so. But once we use for I loop, it returns an iterator. So it does know where it is!
#Iterators also know how to get their next value
#it uses __next__ for next value
#list does not have this. so if i use next() on a list it gives error

# print(next(nums)) #<----TypeError: 'list' object is not an iterator
#Here in background it is trying to run __next__ but list doesnt has one

# Now we know that when we use for loop a __iter__() method is being run
# so, if we try to run that we get:

i_nums = nums.__iter__() #<-- this is what for loop get to us in background!
print(i_nums) #<<----gives: <list_iterator object at 0x000002DA69FD8460>
print(dir(i_nums)) #< -- now let see what methods are allowed here.
# and voila it has __next__ hence it is an iterator now!!
# now
print(next(i_nums)) #<-- This prints out next value of the list as it knows  it state
#Similarly if we do next again:
print(next(i_nums))#<--- This also understand where we left off and gives next value
# just like it being written in the generators.py next value can be only generated until the end of list
#it can be called only len(list) times! so be careful.
# For example, in this list there are 3 items [1,2,3].
# so, if we tried to access more than that, it will cause error
print(next(i_nums))#<<<--- works fine for 3 times printing the next value
# print(next(i_nums))#<--- but causes error on 4th time. So, comment this!
#Now some examples

#but an iterator does not call next all the time.
#basically its doing

i_nums_2 = iter(nums) #<-- This is equivalent to:

while True:
    try:
        item = next(i_nums_2)
        print('new:',item)
    except StopIteration:
        break 


# create class that works like built in range fxn:

class MyRange: #<-- this class acts as a range function that we created on our own
    def __init__(self,start,end):
        self.value = start
        self.end = end

    def __iter__(self): #it has to return iterator
        return self #<-- need to have dunder next method on this
    
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration

        current = self.value
        self.value +=1
        return current 

nums = MyRange(1,10)

# for num in nums: #<-- this is commented so that the lower code could work, else lower code will show stopiteration error!!
#     print(num) 
# Now since it is an iterator we can use __next__ on this class

print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
# print(next(nums)) #<-- stop iteration error in here!!

# so it gives all values

# Now we can make generators out of them!
#generators = easy to use iterators!!

#Generator fxn that does same thing that our range class does

def my_range(start,end):
    current = start
    while current < end:
        yield current #<-- yield is just yielding the next element!
        current += 1

nums2 = my_range(1,10)
print("gen",next(nums2))
print("gen",next(nums2))
print("gen",next(nums2))
print("gen",next(nums2))

# Generators are useful in memory efficient task because it yields multiple values in short time
# an iterator however only gives one iteration as a time

#Recap:
# Iterable- sth that can be looped over. or sth that has returns an iterator obj from its __iter__ method.
# Iterator - The iterable returns iterator using __iter__ method that gives an iterator which knows its position and can find next value using __next__
# Iterator = obj that knows its next value and fetches using __next__
