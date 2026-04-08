#creating file
file=open("sample.txt","w")
file.write("Hello,this is a file handling example.")
file.close()
file=open("sample.txt","r")
content=file.read()
print(content)
file.close()

#Output: Hello,this is a file handling example.

##############################################################
#Context Managers with 'with open()'
with open ("sample.txt","r")as file:
    content=file.read()
    print(content)
    
#Output: Hello,this is a file handling example.

###############################################################
#Error Handling with try/except
try:
    with open("missing.txt","r")as file:
        print(file.read())
except FileNotFoundError:
        print("File not found. Please check the filename.")

#Output: File not found. Please check the filename.

#################################################################
#CSV Parsing
import csv

data = [
    ["Name", "Age", "Marks"],
    ["Alice", 21, 90],
    ["Bob", 19, 89],
    ["Charlie", 18, 91],
    ["David", 20, 92],
    ["John", 22, 90]
]

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

with open("data.csv","r")as file:
    reader=csv.reader(file)
    for row in reader:
      print(row)

#Output:
'''
['Name', 'Age', 'Marks']
['Alice', '21', '90']
['Bob', '19', '89']
['Charlie', '18', '91']
['David', '20', '92']
['John', '22', '90']
'''

####################################################################
from openpyxl import Workbook

data = [
    ["Name", "Age", "Status"],
    ["Alice", 21,"Passed"],
    ["Bob", 19, "Failed"],
    ["Charlie", 18, "Passed"],
    ["David", 20, "Passed"],
    ["John", 22, "Failed"]
]

wb = Workbook()
sheet = wb.active

for row in data:
    sheet.append(row)
    print(row)

wb.save("data.xlsx")

'''
Output:
['Name', 'Age', 'Status']
['Alice', 21, 'Passed']
['Bob', 19, 'Failed']
['Charlie', 18, 'Passed']
['David', 20, 'Passed']
['John', 22, 'Failed']
'''

