import csv

#DictReader will set our keys/values by reading the header
with open('datas.csv') as csv_file:
   reader = csv.DictReader(csv_file, delimiter=',')
   for line in reader:
       print("TITLE : " + line['title'] + "\nDESCRIPTION : " + line['description'] + "\n")
