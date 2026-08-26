# Python reading file (.txt, .json, .csv)

# .txt
file_path = "C:/Users/ACER/python/08-file-io/test.txt"

with open(file_path, "r") as file:
    content = file.read()

print(content)

# .json
import json

with open("person.json", "r") as file:
    data = json.load(file)

print(data)
print(data["name"])
print(data["age"])

# .csv
import csv

with open("people.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)