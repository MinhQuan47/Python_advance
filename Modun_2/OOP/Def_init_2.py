class Cat:
    # class attribute
    species = "cat"
    # non-parametrized constructor
    def __init__(self):
        self.name = "Tom"
        self.color = "grey and white"
    # Methods of Cat class
    def catInfo(self):
        print(self.name, "cat has", self.color,
    "color")

    # create objects of Cat class with non-parametrized constructor
tom1 = Cat()
print("Info of tom1:")
tom1.catInfo()

tom2 = Cat()
print("Info of tom2:")

tom2.catInfo()
tom2.name = "Tom2"
tom2.color = "black and white"
print("Info of tom2 after changed:")
tom2.catInfo()
