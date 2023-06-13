class Cat:
    # class attribute
    species = "cat"
    # constructor of class Cat
    # instance attribute
    def __init__(self, cat_name, cat_color):
        self.name = cat_name
        self.color = cat_color
    # Methods of Cat class
    def catInfo(self):
        print(self.name, "cat has", self.color, "color")
    def catchMouse(self):
        print(self.name, "catch mouse.")
    def sleep(self):
        print(self.name, "take a nap.")
tom = Cat("Tom", "grey and white")

meo = Cat("Meo", "Xam va Trang")

del tom.name
#print("name of tom:", tom.name)

print("name of tom:", meo.name)


""" del tom.name

print("name of tom:", tom.name)
del tom.species

print("species of tom:", tom.species)

 """