# function = กลุ่มคำสั่งที่สามารถนำกลับมาใช้ซ้ำได้ ใส่ () หลังชื่อฟังก์ชันเพื่อเรียกใช้งานฟังก์ชัน

#EX.1
def happy_birthday():
    print("Happy birthday to you!")
    print("You are old!")
    print("Happy birthday to you!")
    print()

happy_birthday("Tle", 21)

#EX.2
def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("Nattawat", 42.50, "01/01")

# return = คำสั่งที่ใช้จบการทำงานของฟังก์ชัน และ ส่งค่าผลลัพธ์กลับไปยังผู้ที่เรียกใช้ฟังก์ชัน

#EX.1
def add(x, y):
    z = x + y
    return z

print(add(1, 2))

#EX.2
def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("nattawat", "lertchidumrongsri")
print(full_name)