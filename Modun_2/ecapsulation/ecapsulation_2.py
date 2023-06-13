class Person:
    def __init__(self):
        self.__age = 20
    def showAge(self):
        print(self.__age)
    def setAge(self, age):
        self.__age = age
    # private method
    def __info():
        print("Info of a person.")
david = Person()
# AttributeError: 'Person' object has no attribute '__age'
print(david.__age)
# AttributeError: 'Person' object has no attribute '__info'
david.__info()
