import csv

with open('D:\Python\Modun_2\File_csv\python_1.csv') as f:
    reader = csv.reader(f, delimiter='-')
    r = [row for row in reader]
print(r)