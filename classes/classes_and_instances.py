# method -> Function that is associated with class

# class Employee:
#     pass

# employee_1 = Employee() #< --- 2 unique instances of Employee class
# employee_2 = Employee()

#---------------------------------------------------------------------------------------------------------------------------------



# class Employee:
#     pass

# employee_1 = Employee()
# employee_2 = Employee()
# employee_1.first = 'Aashish'
# employee_1.second = 'Basnet'
# employee_1.email = 'Aashish@gmaol.com'
# employee_1.pay = 50000

# employee_2.first = 'Animesh'
# employee_2.second = 'Basnet'
# employee_2.email = 'Animesh@gmaol.com'
# employee_2.pay = 60000

# print(employee_1.email)
# print(employee_2.email)   

#--------This above is a manual way of creating instances of class, we can do it without manual too------------
#---------------------------------------------------------------------------------------------------------------------------------

class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last + '@company.com'
    
    def fullname(self):# <--- self is mandatory if u want to run this method, because instance is getting passed in here!!!
        fullname = f'{self.first} {self.last}'
        return fullname
    
emp1 = Employee('Aashish','Basnet',40000)
emp2 = Employee('Animesh','Basnet',30000)

print(emp1.email)
print(emp2.email)   
print(emp1.fullname())
print(Employee.fullname(emp1)) #< --- this also runs, in fact this is what's running in the background!!!