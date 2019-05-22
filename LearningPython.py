#print("Hello")
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def whoAreYou(self):
        print("I am",self.name,"having age:",self.age)

## Inheritance

class Student(Person):

    def __init__(self,name,age,degree):
        Person.__init__(self,name,age)
        self.degree=degree

    def whoAreYou(self):
        #super().whoAreYou() # to call a superView method.
        print("I am",self.name,"having age:",self.age,"curently Pursuing:",self.degree)


robert = Student(name="Robert",age=34,degree="BE")
bob = Student(name="bob",age=39,degree="BE-IT")
#print(robert.whoAreYou())

# to understand iteration
class College:
    def __init__(self,students):
        self.students = students
    def __iter__(self):
        self.index = -1
        return self
    def __next__(self):
        self.index = self.index + 1
        if self.index < len(self.students):
            return self.students[self.index]
        else:
            raise StopIteration


college = College([robert,bob])
for student in college:
    pass#print(student.whoAreYou())

#Module
#import platform # to import an entire module
#print(dir(platform)) # lists all the 
from platform import system # to import a specific part from the module
print(system())
#print(dir(platform))
#print(platform.architecture(),platform.system())
