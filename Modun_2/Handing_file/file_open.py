# fuc read()
f = open("D:\Python\Modun_2\Handing_file\python.txt","rt",encoding="utf-8")
print(f.read())

print("--------------------------------------------------")


f_1 = open("D:\Python\Modun_2\Handing_file\python.txt","rt",encoding="utf-8")
print(f_1.read(5))

#  fuc readine()
print("--------------------------------------------------")
f_2 = open("D:\Python\Modun_2\Handing_file\python.txt","rt",encoding="utf-8") 
print(f_2.readline(), end='') 

# fuc close 
f_2.close
print("--------------------------------------------------")

# for 
f_2 = open("D:\Python\Modun_2\Handing_file\python.txt","rt",encoding="utf-8") 
for i in range(2):
    print(f_2.readline(), end='') 
