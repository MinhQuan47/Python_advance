import csv
with open('D:\Python\Modun_2\File_csv\python.csv') as f:
    reader = csv.reader(f)
    r = [row for row in reader]
print(r)

print(r[1])

print(r[1][1])