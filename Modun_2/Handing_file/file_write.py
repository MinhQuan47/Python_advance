
# a : ghi nối vào file
f = open("D:\Python\Modun_2\Handing_file\python.txt","a",encoding="utf-8")
f.write("\nWelcome to the Python PCAP class!") 
f.close()

# w : ghi đè lên file
f = open("D:\Python\Modun_2\Handing_file\python.txt","w",encoding="utf-8")
f.write("\nWelcome to the Python PCAP class!") 
f.close()

f = open("D:\Python\Modun_2\Handing_file\python.txt","rt",encoding="utf-8")
print(f.read()) 
f.close()