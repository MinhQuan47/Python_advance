import csv
with open('D:\Python\Modun_2\File_csv\python.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)