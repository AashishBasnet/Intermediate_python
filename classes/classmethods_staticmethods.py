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
    
    @classmethod
    def set_raise_amt(cls,amount): #<--cls = common convention for class
        cls.raise_amount = amount

    @classmethod
    def from_string(cls,emp_str):
        first,last, pay = emp_str.split('-')
        return cls(first,last,pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 4:
            return False
        return True

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

#but --now with class method also: 

Employee.set_raise_amt(1.09)

print("class method: ",Employee.raise_amount) 
print(emp1.raise_amount)
print(emp2.raise_amount)

 
emp1.set_raise_amt(1.03) #<---even from instance it changes for all

print("class method from instance: ",Employee.raise_amount) 
print(emp1.raise_amount)
print(emp2.raise_amount)


#class methods as alternative constructor

#let's say we are making new instances from data like this:
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'
# we can do such thing by this way:
# first,last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first,last,pay)

# print("new emp email: ",new_emp_1.email)

#but let's make constructor such that this process is done without parsing str every time

#THerefore alternative constructor can be used as class method
#Therefore now:

new_emp_1 = Employee.from_string(emp_str_1)
new_emp_2 = Employee.from_string(emp_str_2)
new_emp_3 = Employee.from_string(emp_str_3)
print(new_emp_1.__dict__)
print(new_emp_2.__dict__)
print(new_emp_3.__dict__)


import datetime
my_date = datetime.date(2016, 7 , 16)

print(Employee.is_workday(my_date))