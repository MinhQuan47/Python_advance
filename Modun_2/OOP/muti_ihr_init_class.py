#__init__ trong da ke thua
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(self.name + ",", self.age, "years old.")
        
class Employee:
    def __init__(self, salary):
        self.salary = salary
    def showSalary(self):
        print("salary:", self.salary)

class Teacher(Person, Employee):
    def __init__(self, name, age,salary):
        super().__init__(name , age)
        self.salary = salary

print(Teacher.mro())
john = Teacher("John", 35 ,200)
# call method inherits from Person
john.info()
# AttributeError: 'Teacher' object has no attribute 
'salary'
john.showSalary()
