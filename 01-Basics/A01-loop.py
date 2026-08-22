# while loop = ทำงานบางอย่างซ้ำ ๆ ตราบใดที่เงื่อนไขยังคงเป็น True

#EX.1
name = input()

while name == "":
    print("You did not enter your name")
    name = input()

print(f"Hello {name}")

#EX.2
food = input()

while not food == "q":
    print(f"You like {food}")
    food = input()

print("bye")

# for loops = ทำงานชุดคำสั่งซ้ำตามจำนวนครั้งที่กำหนด
#             สามารถวนซ้ำผ่าน range, string, sequence และอื่น ๆ ได้

#EX.1
for x in range(1, 11):
    print(x)

#EX.2
for x in reversed(range(1, 11)):
    print(x)

#EX.3
for x in range(1, 11, 3):
    print(x)

#EX.4
credit_card = "1234-5678-9012-3456"

for x in credit_card:
    print(x)

#EX.5
for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)

#EX.6
for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)

# nested loop = ลูปที่อยู่ภายในลูปอีกชั้นหนึ่ง (outer, inner)
#               outer loop = ลูปด้านนอก
#                   inner loop = ลูปด้านใน

#EX.1
for x in range(1, 10):
    print(x, end="") # 123456789

#EX.2
for x in range(3):
    for y in range(1, 10):
        print(x, end="")
    print()