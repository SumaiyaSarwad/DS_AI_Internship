#Task 2: The CSV Student List (Data Ingestion)
import csv

data = [
    ["Name", "Grades", "Status"],
    ["Alice", "A", "Pass"],
    ["Bob", "B","Pass"],
    ["Charlie","F", "Fail"]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

with open("students.csv","r")as file:
    reader=csv.reader(file)
    for row in reader:
        if row[2]=="Pass":
            print(row[0])

'''
Output:
Alice
Bob
'''
