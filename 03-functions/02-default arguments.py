# default arguments = ค่าพารามิเตอร์เริ่มต้น จะใช้ค่าเริ่มต้นเมื่อไม่ได้ระบุ argument นั้น
#                    ทำให้ฟังก์ชันมีความยืดหยุ่นมากขึ้น และลดจำนวน argument ที่ต้องส่ง
#                    1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary

#EX.1
def net_price(list_price, discount = 0, tax = 0.05):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500)) # 525.0
print(net_price(500, 0.1)) # 472.5
print(net_price(500, 0.1, 0)) # 450.0

#EX.2
import time

def count(end, start = 0):
    for x in range(start, end + 1):
        print(x)
        time.sleep(1)
    print("DONE!")

count(10)
count(30, 15)