# format specifiers = ตัวกำหนดรูปแบบ ใช้จัดรูปแบบค่าตาม flags ที่ใส่เข้าไป
#                     {value:flags}

# .(number)f = ปัดเศษให้มีทศนิยมตามจำนวนที่กำหนด (fixed point)
# :(number)  = จัดสรรพื้นที่ให้มีจำนวนช่องว่างตามที่กำหนด
# :03        = จัดสรรพื้นที่และเติม 0 ให้ครบตามจำนวนช่องที่กำหนด
# :<         = จัดชิดซ้าย
# :>         = จัดชิดขวา
# :^         = จัดให้อยู่ตรงกลาง
# :+         = แสดงเครื่องหมาย + สำหรับค่าที่เป็นบวก
# :=         = วางเครื่องหมายไว้ทางซ้ายสุด
# :          = เพิ่มช่องว่างหน้าตัวเลขที่เป็นบวก
# :,         = ใช้เครื่องหมาย comma (,) คั่นหลักตัวเลข

price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"Price 1 is {price1:.2f}") # Price 1 is 3.14
print(f"Price 2 is {price2:10}")  # Price 2 is    -987.65
print(f"Price 3 is {price3:010}") # Price 3 is 0000012.34

print(f"Price 1 is {price1:<10}") # Price 1 is 3.14159
print(f"Price 2 is {price2:>10}") # Price 2 is    -987.65
print(f"Price 3 is {price3:^10}") # Price 3 is   12.34    

print(f"Price 1 is {price1:+}") # Price 1 is +3.14159
print(f"Price 2 is {price2:+}") # Price 2 is -987.65
print(f"Price 3 is {price3:+}") # Price 3 is +12.34    

print(f"Price 1 is {price1: }") # Price 1 is  3.14159
print(f"Price 2 is {price2: }") # Price 2 is -987.65
print(f"Price 3 is {price3: }") # Price 3 is  12.34

print(f"Price 1 is {price1:+,.2f}")
