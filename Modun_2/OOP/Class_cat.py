class Cat:
# Properties of Cat class
    name = "Tom"
    color = "grey and white"
# Methods of Cat class
    def catch_Mouse(self):
        print(self.name, "catches Jerry mouse.")
    def sleep(self):
        print(self.name, "takes a nap.")
# create an object of Cat class
tom = Cat()
print(tom.name)
print(tom.color)
tom.catch_Mouse()
tom.sleep()
