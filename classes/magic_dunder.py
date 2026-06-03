class Employee:
    num_of_emps = 0
    raise_amount = 1.04
    def __init__(self,first,last,pay): #<--This is a magic/dunder function:: dunder = double underscore
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last + '@company.com'
        Employee.num_of_emps +=1 

    def fullname(self):
        fullname = f'{self.first} {self.last}'
        return fullname
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self) : #<-- unambiguous representation of an object, used for debugging and logging, meant to be seen by other developers
        return f"Employee({self.first}, {self.last}, {self.pay})"
    def __str__(self): #<--- The str dunder fxn overwrites the repr
        return f"{self.fullname()} - {self.email}" 
    
    def __add__(self,other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())



emp1 = Employee('Aashish','Basnet',40000)
emp2 = Employee('Animesh','Basnet',30000)

print(emp1)
print(repr(emp1)) #<--- can access the specific dunder fxn like this!
print(str(emp1))

print(1+2) #<---- this is actually using a dunder __add__ function
print(int.__add__(1,2)) #<--- this is the dunder fxn used by python to add 2 variables in int data type
print(str.__add__('a','b')) #<-- similarly, for string the dunder add concatenates them

print(emp1 + emp2) #<--- now we can use dunder add method to add salaries of 2 employees

#Similarly another special method len:

print(len('test'))

print('test'.__len__()) #<--- same thing as len ('test')

print(len(emp1)) #<-- This gives the length of string of full name of emp1 by accessing it through the instance!