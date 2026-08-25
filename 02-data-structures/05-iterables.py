# Iterables = อ็อบเจกต์หรือ collection ที่สามารถคืนสมาชิกออกมาทีละตัว
#             ทำให้สามารถวนซ้ำสมาชิกเหล่านั้นด้วย loop ได้

numbers = [1, 2, 3, 4, 5]

#EX.1
for item in numbers:
    print(item)

#EX.2
for item in reversed(numbers):
    print(item)

#EX.3
name = "Nattawat"

for character in name:
    print(character, end=" ")

#EX.4
my_dictionary = {"A": 1, "B": 2, "C": 3}

for key, value in my_dictionary.items():
    print(f"{key} = {value}")