import csv
with open('D:\Python\Modun_2\File_csv\python.csv') as f:
    reader = csv.reader(f)
    r = [row for row in reader]
l_hoandoi = [list(x) for x in zip(*r)]
print(l_hoandoi)

print(l_hoandoi[0])

