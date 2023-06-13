class Cat:
# parameterized constructor
    def __init__(self, cat_name, cat_color="grey and white", cat_weight=3.9):
        self.name = cat_name
        self.color = cat_color
        self.weight = cat_weight
    # Methods of Cat class
    def catInfo(self):
        print(self.name, "cat has", self.color, "color, weight", self.weight)
    # create objects of Cat class with parameterized constructor
tom = Cat("Tom")
tom.catInfo()
mycat = Cat("Milk", "black and white")
mycat.catInfo()
myfriendcat = Cat("MeoMeo", "black and white", 4.5)
myfriendcat.catInfo()
