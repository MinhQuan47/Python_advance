import csv
import pprint
csv_path = 'D:\Python\Modun_2\File_csv\python.csv'
with open(csv_path) as f:
    reader = csv.DictReader(f)
    r = [row for row in reader]
pprint.pprint(r)