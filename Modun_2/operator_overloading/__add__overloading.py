class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "({0},{1})".format(self.x, self.y)
    # define special function __add__ 
    def __add__(self, apoint):
        x = self.x + apoint.x
        y = self.y + apoint.y
        return Point(x, y)
# create objects of Point
p1 = Point(1, 2)
p2 = Point(2, 3)
p3 = Point(2, 3)
p4 = p1 + p2 +p3
p5 = p4 +p3
print(p4)
print(p5)
