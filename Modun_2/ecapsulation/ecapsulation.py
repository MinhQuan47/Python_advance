class Person:
    def __init__(self):
        self.__age = 20
    def showAge(self):
        print(self.__age)
    def setAge(self, age):
        self.__age = age
david = Person()
print("Age of david: ", end='')
david.showAge()
david.__age = 99
print("Age of david after david.__age = 99: ", end='')
david.showAge()
david.setAge(99)
print("Age of david after david.setAge(99): ", end='')
david.showAge()
