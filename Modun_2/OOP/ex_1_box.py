''' Tạo thuộc tính box bằng class với các thuộc tính : dài , rộng ,cao
    Tạo thuộc tính màu sắc ,vật liệu của box
    Tạo hàm xây dựng để nhập kích thước dài , rộng ,cao , màu sắc , vật liệu 
    Tạo hàm tính thể tích của hộp
    Tạo hàm in thông tin của box '''


class box:
    mausac = "Ghi"
    vatlieu = "Nhua"
    def __init__(self, _dai, _rong,_cao):
        self.dai = _dai
        self.rong = _rong
        self.cao = _cao
    
    def thetich(self):
        return self.dai*self.rong*self.cao
    
    def inbox(self):
        print("Thong tin box:")
        print("Mau sac: ",self.mausac)
        print("vat lieu: ",self.vatlieu)
        print("Rong: ",self.rong)
        print("Cao: ",self.cao)
        print("Sau: ",self.dai)
    
    def nhapdl(self):
        r = int(input("Chieu rong: "))
        c = int(input("Chieu cao: "))
        s = int(input("Chieu sau: "))
        self.rong = r
        self.cao = c
        self.dai = s
#Tao doi tuong

hh = box(5, 4, 3)      
hh.inbox()
print("The tich: ",hh.thetich())

hh.mausac = "Do"
hh.vatlieu = "Cao su"
hh.dai = 10
hh.rong = 8
hh.cao = 15
hh.inbox()

print("The tich: ",hh.thetich())

print("-------------------------------------")
hh.nhapdl()
hh.inbox()
print("The tich: ",hh.thetich())
print("-------------------------------------")
del hh
hh.inbox()