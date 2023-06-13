import os 
os.remove("D:\Python\Modun_2\Handing_file\python.txt")

# Kiểm tra một file xem có tồn tại hay ko để xóa file đó đi
if os.path.exists("python.txt"): 
    os.remove("python.txt") 
else: 
    print("The file does not exist.")
