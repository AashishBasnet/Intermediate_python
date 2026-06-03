# collections: counter, namedtuple, OrderedDict, defaultdict, deque

from collections import Counter #<- container storing elements as dict keys and their count as values
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque

a = "aaaaaabbbbccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(1))
print(list(my_counter.elements()))

point_2d = namedtuple('Point', 'x,y') #<----creates class called 'point' with the fields x and y
pt = point_2d(1,-4)
print(pt)
print(pt.x,pt.y)

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4

print(ordered_dict)


d = defaultdict(int)
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4

print(d['e']) #<---No key error even if the value doesn't exist

d = deque()

d.append(1)
d.append(2)
d.appendleft(3)
print(d)
d.pop() #<- popleft() can also be used
print(d)
d.extendleft([4,5,6])
print(d)
d.rotate(1)# <-rotate 1 place to the right can also use 2,3,etc
print(d)
d.clear()#<---removes all element
print(d)