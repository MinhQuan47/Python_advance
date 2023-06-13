class Person: 
    def info(self): 
        print("Info of a person.") 
class Employee: 
    def showSalary(self): 
        print("Salary of an employee.") 
class Teacher(Person, Employee): 
    pass
john = Teacher() 
john.info() 
john.showSalary()