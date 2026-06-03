# PROPERTY DECORATORS are the getters, setters and Deleters of python!

class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
    @property
    def email(self):
        fullname = f'{self.first}.{self.last}@email.com'
        return fullname
    @property
    def fullname(self):
        fullname = f'{self.first} {self.last}'
        return fullname
    @fullname.setter
    def fullname(self,name):
        first,last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None
emp1 = Employee('Aashish','Basnet',40000)

emp1.first = 'Ramesh'
print(emp1.first)
print(emp1.email) #<--- Here after using @property decorator we dont need to use parenthesis here!!!
print(emp1.fullname)
emp1.fullname = 'Animesh Basnet'
print(emp1.fullname)
print(emp1.first)
del emp1.fullname
print(emp1.fullname)
print(emp1.first)