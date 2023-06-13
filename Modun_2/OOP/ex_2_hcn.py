"""Tao lop diem voi 2 thuoc tinh x, y va phuong thuc indiem

Tao lop HCN ke thua lop diem - 4 dinh HCN la 4 diem

yeu cau:

1. Tao phuong thuc tinh chieu dai, chieu rong HCN

2. Tao phuong thuc tinh chu vi HCN

3. Tao phuong thuc tinh dien tich HCN

4. Tao phuong thuc in thong tin HCN"""



import math
class diem():
    def __init__(self,x,y):

        self.x = x
        self.y = y

    def indiem(self):

        print("Diem co toa do: ",self.x,",",self.y)

class hcn(diem):

    d1 = diem(0,0)
    d3 = diem(0,0)
    def __init__(self, x, y, d1, d3):

        super().__init__(x, y)
        self.d1.x = d1.x
        self.d1.y = d1.y
        self.d3.x = d3.x
        self.d3.y = d3.y

    def chieudai(self):

        if self.d3.x != self.d1.x:
            return abs(self.d3.x - self.d1.x)
        else:
            return 0 

    def chieurong(self):

        if self.d3.y != self.d1.y:
            return abs(self.d3.y - self.d1.y)
        else:
            return 0

    def chuvi(self):

        if self.chieudai()>0 and self.chieurong()>0:
            return 2*(self.chieudai() + self.chieurong())
        else:
            return 0
    
    def dientich(self):

        if self.chieudai()>0 and self.chieurong()>0:
            return self.chieudai() * self.chieurong()
        else:
            return 0
            
    def inhcn(self):

        if self.chieudai()>0 and self.chieurong()>0:
            print("Chieu dai:",self.chieudai())
            print("Chieu rong:",self.chieurong())
            print("Chu vi:",self.chuvi())
            print("Dien tich:",self.dientich())
        else:
            print("Cac goc cua HCN khong le!")

d1 = diem(0,8)
d2 = diem(10,0)
h = hcn(0,0,d1,d2)
h.inhcn()               