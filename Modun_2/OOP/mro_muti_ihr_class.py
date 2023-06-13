class Person:
    def info(self):
        print("Info of a person.")
    def work(self):
        print("A person works.")
class Employee:
    def work(self):
        print("An employee works.")
    def showSalary(self):
        print("Salary of an employee.")
class Teacher(Person, Employee):
    pass
print(Teacher.__mro__)
john = Teacher()
john.work()
