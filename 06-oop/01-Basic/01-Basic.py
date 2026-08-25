# object = "กลุ่ม" ของ attributes (ตัวแปร) และ methods (ฟังก์ชัน) ที่เกี่ยวข้องกัน
#          เช่น phone, cup, book
#          ต้องมี "class" เพื่อใช้สร้าง object หลาย ๆ ตัว

# class = แบบพิมพ์เขียว (blueprint) ที่ใช้กำหนดโครงสร้างและรูปแบบของ object

from car import Car

car1 = Car("Mustang", 2024, "red", False)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

car1.drive()
car1.stop()