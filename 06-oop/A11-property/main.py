# @property = Decorator ที่ใช้กำหนด Method ให้ทำงานเหมือน Property
#             ทำให้สามารถเข้าถึง Method ได้เหมือน Attribute
#             ข้อดี: สามารถเพิ่มเงื่อนไขหรือ Logic ตอนอ่าน แก้ไข หรือลบ Attribute ได้
#             สามารถใช้สร้าง Getter, Setter และ Deleter ได้

from rectangle import Rectangle

rectangle = Rectangle(3, 4)

rectangle.width = 5
rectangle.height = 6

print(rectangle.width)
print(rectangle.height)

del rectangle.width
del rectangle.height
