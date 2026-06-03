my_set = set()

my_set.add(1)
my_set.add(2)
my_set.add(3)

print(my_set.pop()) #<---removes and returns first element

print(my_set)


#---loop set

for x in my_set:
    print(x)

if 2 in my_set:
    print('yes')


odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}

u = odds.union(evens)
print(u)

i = odds.intersection(primes)
print(i)

ie = evens.intersection(primes)
print(ie)

d = odds.difference(primes)
print(d)

d2 = primes.difference(evens)
print(d2)

sym_diff = odds.symmetric_difference(primes) # <---- Takes both set a and B values but not if common
print(sym_diff)

# to_modify sets

setA = {1,2,3,11,12,13,14,15}
setA.update(primes)
print(setA)
setA.intersection_update(odds)
print(setA)
setA.difference_update(evens)
print(setA)
setA.symmetric_difference_update(primes)
print(setA)

setA = {1,2,3,11,12,13,14,15}
setB = {1,2,3,11,12,13}

print(setA.issubset(setB))
print(setB.issubset(setA))
print(setB.issuperset(setA))
print(setA.issuperset(setB))
# < --------------    Ans = False True False True

print(setA.isdisjoint(setB)) #< ---- False
setC = {100,200,300}

print(setA.isdisjoint(setC)) #< --- True


# -------------------- Set assignment

# simple assignment
setD = {1,2,3}
setE = setD
# but  if change then it changes original set i.e

setE.add(100)

print(setE)
print(setD)

# Another way of copying that does not affect original
setE = setD.copy()
setE.add(200)

print(setE)
print(setD)

#final way
setE = set(setD)
setE.add(200)

print(setE)
print(setD)

# THe frozen set --- A collection data type, immutable version of normal set

a = frozenset([1,2,3,4])

# a.add(2) #<---- Gives error in frozen set because immutable
#------------ can do union, intersection, etc though!!!
print(a)