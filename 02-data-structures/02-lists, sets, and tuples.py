# collection = "ตัวแปร" ตัวเดียวที่ใช้เก็บค่าหลายค่า
#   List  = [] มีลำดับและสามารถเปลี่ยนแปลงได้ สามารถมีค่าซ้ำได้
#   Set   = {} ไม่มีลำดับและไม่สามารถเปลี่ยนแปลงสมาชิกเดิมได้ แต่สามารถเพิ่ม/ลบสมาชิกได้ ห้ามมีค่าซ้ำ
#   Tuple = () มีลำดับและไม่สามารถเปลี่ยนแปลงได้ สามารถมีค่าซ้ำได้ และทำงานได้เร็วกว่า
#              ทั้ง List, Set และ Tuple สามารถเก็บสมาชิกที่มี ชนิดข้อมูลต่างกัน ได้

# List
fruits = ["apple", "orange", "banana", "coconut"]
print(fruits)      # ['apple', 'orange', 'banana', 'coconut']
print(fruits[0])   # ['apple']
print(fruits[:3])  # ['apple', 'orange', 'banana']
print(fruits[::2]) # ['apple', 'banana']
print(dir(fruits))  # ดูว่า object หรือตัวแปรนั้นมีอะไรให้เราใช้งานได้บ้าง เช่น methods และ attributes
print(help(fruits)) # ดูคำอธิบายและวิธีใช้งาน ของสิ่งต่าง ๆ เช่น function, class, method หรือ object
print(len(fruits))  # 4
print("pineapple" in fruits) # False
fruits[0] = "pineapple" # แก้ค่า
fruits.append("pineapple") # เพิ่มไปที่ตอนท้าย
fruits.remove("pineapple") # ลบตัวที่เลือก
fruits.insert(0, "pineapple") # แทรกตัวไปยังตำแหน่งที่เลือก
fruits.sort()    # เรียงลำดับ
fruits.reverse() # กลับลำดับ
fruits.clear()   # ลบสมาชิกทั้งหมด
print(fruits.index("apple")) # 0
fruits.count("banana") # นับค่า
new_fruits = fruits.copy() # copy ค่า
fruits.pop(1) # ลบด้วย index

# Set
fruits = {"apple", "orange", "banana", "coconut"}
print(fruits)  # {'apple', 'orange', 'banana', 'coconut'}
print(dir(fruits))
print(help(fruits))
print(len(fruits))
print("pineapple" in fruits)
fruits.add("pineapple")
fruits.remove("apple") #ลบค่าที่ระบุ
fruits.pop()   # ลบสมาชิกออก 1 ตัวแบบไม่ระบุว่าเป็นตัวไหน
fruits.clear() # ล้างสมาชิก
fruits.discard("apple")            # ลบค่าที่ระบุ ถ้าไม่มีจะไม่ Error
fruits.update(["mango", "grape"])  # เพิ่มสมาชิกหลายตัว

a = {"apple", "banana", "orange"}
b = {"banana", "orange", "mango"}

a.union(b)          # {'apple', 'banana', 'orange', 'mango'} หรือใช้ a | b
a.intersection(b)   # {'banana', 'orange'} หรือใช้ a & b
a.difference(b)     # {'apple'} หรือใช้ a - b
a.symmetric_difference(b) # {'apple', 'mango'} สมาชิกที่ไม่ซ้ำกันระหว่างสอง Set หรือใช้ a ^ b

# Tuple
fruits = ("apple", "orange", "banana", "coconut")
print(dir(fruits))
print(help(fruits))
print(len(fruits))
print("pineapple" in fruits)
print(fruits.index("apple")) # 0
fruits.count("banana") # นับค่า
