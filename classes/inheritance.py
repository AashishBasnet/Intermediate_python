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
    
class Developer(Employee):# <--- inherited from employee class
     raise_amount = 1.10 #<---now this raise_amount overrides the one in parent

     def __init__(self,first,last,pay,prog_lang): 
            super().__init__(first,last,pay) #<---This lets the Employee class handle it
            # Employee.__init__(self,first,last,pay) #<--This also works
            self.prog_lang = prog_lang 

class Manager(Employee):
    def __init__(self,first,last,pay,employees = None):#<- an empty list wasn't passed as default arg here because you don't pass mutables this way!
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_employee(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
        else:
            print("The employee is already in the list!")
    
    def remove_employee(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
        else:
            print("The employee is not on the list!")
    
    def list_employees(self):
        for emp in self.employees:
            print('-->',emp.fullname())

emp1 = Developer('Aashish','Basnet',40000,'Python') #<-- after inheriting the class employee, this code works too!
emp2 = Developer('Animesh','Basnet',30000,'Java')


mgr_1 = Manager('Ramesh','Basnet',90000,[emp1]) #<-- This is our manager instance

print(mgr_1.email)
mgr_1.list_employees()
mgr_1.add_employee(emp2)
mgr_1.list_employees()
mgr_1.remove_employee(emp1)
mgr_1.list_employees()
# These inherited classes are very useful because they let us have functionalities that are important to one sub class


# print(help(Developer)) #<--goes to Developer class and if it doesn't find it here, goes to the builtins.object

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)

# Two built in functions:

print(isinstance(mgr_1,Manager))
print(isinstance(mgr_1,Employee))
print(isinstance(mgr_1,Developer)) #<--since this subclass is not related to Manager, developers cannot run functions specific to managers!

# Similarly another built in function to check whether a class is subclass of other:
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))
print(issubclass(Employee, Developer))

