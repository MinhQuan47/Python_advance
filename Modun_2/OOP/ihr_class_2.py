class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(self.name + ",", self.age, "years old.")
# Student inherits from Person

class Student(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.id = id
    def infoStudent(self):
        print(self.name + ",", self.age, "years old, id:", self.id)
son = Student("Son", 30, "0868608378")
son.infoStudent()
