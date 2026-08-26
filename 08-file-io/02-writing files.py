# Python writing file (.txt, .json, .csv)

# .txt
txt_data = "I like pizza!"

file_path = "output.txt"

try:
    with open(file_path, "w") as file:
        file.write(txt_data)
        print(f"txt file {file_path} was created")
except FileExistsError:
    print("That file already exists!")

# .json
import json

data = {
    "name": "Tle",
    "age": 20,
    "language": "Python"
}

with open("person.json", "w") as file:
    json.dump(data, file, indent=4)

# .csv
import csv

data = [
    ["Name", "Age"],
    ["Tle", 20],
    ["John", 25]
]

with open("people.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)