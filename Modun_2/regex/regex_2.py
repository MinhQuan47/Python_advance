import re

str = "Python PCAP! Regex trong Python."
matches = re.search("PCAP", str)
print(matches.span())
print(matches.group())
print(matches.string)

print("-----------------------------------------------------------------------")

# fuc split
str ="Python PCAP BKACAD"
x = re.split("\s", str, 1) 
# \s : tách khoảng trắng 
# ( , , 1) : 1 là chia số phần tử 
y = re.split("\s", str, 2)
print(x)
print(y)

print("-----------------------------------------------------------------------")

# fuc sub
str = "Python PCAP BKACAD"
x = re.sub("A", "a", str) 
y = re.sub("A", "a", str, 2) # – khống chế số lần thay
print(x)
print(y)



