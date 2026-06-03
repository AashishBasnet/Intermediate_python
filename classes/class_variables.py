class Employee:
    num_of_emps = 0
    raise_amount = 1.04
    def __init__(self,first,last,pay): ##<---runs every time new instance is created
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last + '@company.com'
        Employee.num_of_emps +=1 #<---Here we don't need self, because it should not be overwritten! and it needs to be incremented!

    def fullname(self):# <--- self is mandatory if u want to run this method, because instance is getting passed in here!!!
        fullname = f'{self.first} {self.last}'
        return fullname
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
emp1 = Employee('Aashish','Basnet',40000)
emp2 = Employee('Animesh','Basnet',30000)

print(emp1.email)
print(emp2.email)   
print(emp1.fullname())
print(Employee.fullname(emp1)) #< --- this also runs, in fact this is what's running in the background!!!
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)

# print(Employee.raise_amount) #<---can access from all these
# print(emp1.raise_amount)
# print(emp2.raise_amount)

Employee.raise_amount = 1.05

print(Employee.raise_amount) 
print(emp1.raise_amount)
print(emp2.raise_amount)

#but

emp1.raise_amount = 1.06

print(emp1.__dict__)
print(Employee.raise_amount) 
print(emp1.raise_amount) #<-- only this changes
print(emp2.raise_amount)

print(Employee.num_of_emps)