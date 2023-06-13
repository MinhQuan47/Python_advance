class Data:
    def __init__(self, i):
        self.id = i
    def __bool__(self):
        return self.id % 2 == 0
d1 = Data(6)
d2 = Data(4)
# False
print(bool(Data(3)) and bool(Data(4)))
