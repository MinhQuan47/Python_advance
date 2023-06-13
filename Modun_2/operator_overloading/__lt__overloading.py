class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    # define special function __str__() 
    def __str__(self):
        return "({0},{1})".format(self.x, self.y)
    # define special function __lt__ 
    def __lt__(self, apoint):
        self_mag = (self.x ** 2) + (self.y ** 2)
        apoint_mag = (apoint.x ** 2) + (apoint.y ** 2)
        return self_mag < apoint_mag
    # create objects of Point
p1 = Point(1, 2)
p2 = Point(2, 3)
p3 = Point(-1, 1)
print("p1<p2?", p1<p2)
print("p1<p3?", p1<p3)
print("p2<p3?", p2<p3)
