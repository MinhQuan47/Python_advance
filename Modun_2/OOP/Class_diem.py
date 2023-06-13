import math

class diem:
    x = 0
    y = 0
    def kc(self):
        return math.sqrt(self.x*self.x+self.y*self.y)
d = diem()
d.x = 10
d.y = 30

print("Khoang cach tu diem d den goc toa do la: ",d.kc())
#Tao 3 diem bat ky, kiem tra xem 3 diem do co tao thanh 3 dinh tam giac khong

d1 = diem()
d2 = diem()
d3 = diem()

d1.x = -5
d1.y = 0
d2.x = 20
d2.y = 35
d3.x = -5
d3.y = 2

d1d2 = math.sqrt(math.pow(d2.x-d1.x,2) + math.pow(d2.y-d1.y,2))

d1d3 = math.sqrt(math.pow(d3.x-d1.x,2) + math.pow(d3.y-d1.y,2))

d2d3 = math.sqrt(math.pow(d3.x-d2.x,2) + math.pow(d3.y-d2.y,2))



if d1d2+d1d3>d2d3 and d1d2+d2d3>d1d3 and d1d3+d2d3>d1d2:
    
    if d1d2 == d1d3 == d2d3 :
        print(" 3 diem d1 d2 d3 tao thanh 3 dinh cua tam giac deu ")
    elif d1d2 == d1d3 or d1d3 == d2d3 or d1d2 == d2d3:
        print("3 diem d1 d2 d3 tao thanh 3 dinh cua tam giac can ")
    elif d1d2*d1d2 + d1d3*d1d3 == d2d3*d2d3 or d2d3*d2d3 + d1d3*d1d3 ==  d1d2*d1d2 or d1d2*d1d2 + d2d3*d2d3 == d1d3*d1d3:
        print(" 3 diem d1 d2 d3 tao thanh 3 dinh cua tam giac vuong ")
    else:
        print("3 diem d1 d2 d3 là 3 canh cua mot tam giac ")
else:

    print("3 diem d1, d2 d3 KHONG tao thanh 3 dinh cua tam giac!")




'''Tao ra mang gom n diem, tinh khoang cach tu cac diem den goc toa do. Cho biet diem nam
gan, xa goc toa do nhat'''

