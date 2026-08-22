# input() = ฟังก์ชันที่ให้ผู้ใช้ป้อนข้อมูล คืนค่าข้อมูลที่ผู้ใช้ป้อนเข้ามาในรูปแบบ string

name = input("What is your name?: ")
age = int(input("How old are you?: "))

print(f"Hello {name}!")
print(f"You are {age} years old")

# Exercise 1 Rectangle Area Calc

length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = width * length

print(f"The area is: {area}cm")