lines = ['Hello all, welcome to Python PCAP!', 
'Very happy to see you visit Python PCAP class.', 
'Hope it might be useful for you!'] 

f = open("D:\Python\Modun_2\Handing_file\python.txt", "w") 
for line in lines: 
    f.write(line) 
    f.write('\n') 
f.close() 
#open and read the file after overwriting
f = open("python.txt", "r") 
print(f.read()) 
f.close()