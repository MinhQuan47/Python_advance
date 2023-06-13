class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(self.name + ",", self.age, "years old.") # Student inherits from Person
class Student(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.id = id
    def info(self):
        print(self.name + ",", self.age, "years old, id:", self.id)
        print("Is Student subclass of Person?", issubclass(Student,Person))
        print("Is Person subclass of Student?", issubclass(Person,Student)) 
        print("\n")
# create objects
kane = Person("Kane", 29) 
print("Is kane an instance of Person?", isinstance(kane, Person))
print("Is kane an instance of Student?", isinstance(kane, Student))
son = Student("Son", 30, "0469191517") 
print("Is son an instance of Person?", isinstance(son, Person)) 
print("Is son an instance of Student?", isinstance(son, Student)) 
print("\n") 
# type of kane and son

print("Type of kane:", type(kane)) 
print("Type of son:", type(son))
