import csv
import openpyxl

csv_data=[]
with open('sample.csv', 'r') as file_obj:
    reader = csv.reader(file_obj)
    for row in reader:
        csv_data.append(row)
workbook = openpyxl.Workbook()
sheet = workbook.active
for row in csv_data:
    sheet.append(row)
    workbook.save('sample.xlsx')
    print("Success! File saved.")
except PermissionError:
    print("Error: Please close 'sample.xlsx' in Excel and try again!")
