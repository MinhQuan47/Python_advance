#Ke thua nhieu cap
class Base:
    def methodBase(self):
        print("This is a method of Base.")
class Derived1(Base):
    def methodDerived1(self):
        print("This is a method of Derived1.")
class Derived2(Derived1):
    def methodDerived2(self):
        print("This is a method of Derived2.")
# create an object of Derived2
obj = Derived2()
# call method inherits from Base
obj.methodBase()
# call method inherits from Derived1
obj.methodDerived1()
# call method of Derived2
obj.methodDerived2()
