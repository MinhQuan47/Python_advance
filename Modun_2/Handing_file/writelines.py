lines = ['Hello all, welcome to Python PCAP!', 
'Very happy to see you visit Python PCAP', 
'Hope it might be useful for you!'] 

f = open("D:\Python\Modun_2\Handing_file\python.txt", "w") 
f.writelines('\n'.join(lines)) 
f.close() 

#open and read the file after overwriting
f = open("python.txt", "r") 
print(f.read()) 
f.close()
