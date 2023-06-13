import csv
csv_path = 'D:\Python\Modun_2\File_csv\python.csv'
with open(csv_path) as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)