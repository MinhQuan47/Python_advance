class Cat:
# Properties of Cat class
    name = "Tom"
    color = "grey and white"
# Methods of Cat class
    def catchMouse(self):
        print(self.name, "catches Jerry mouse.")
    def sleep(self):
        print(self.name, "takes a nap.")
tom = Cat()
print("Before delete tom object:", tom)
del tom
print("After delete tom object:", tom)