from ssl import MemoryBIO


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
tom.catInfo()
mycat = Cat("Milk", "black and white")
mycat.catInfo()

ten = "meooo" 
mau = "xanh" 
meocon = Cat(ten,mau)
print("mèo con", meocon.name , "màu",meocon.color)

t = input("Nhập tên mèo ")
m = input("Nhập tên màu")
meo_con = Cat(t,m)
print("mèo con", meo_con.name , "màu",meo_con.color)